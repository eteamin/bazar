# -*- coding: utf-8 -*-
from cgi import FieldStorage

import transaction
from tg import expose, abort, session, flash, lurl, redirect
from tg.exceptions import HTTPFound
from tg.i18n import ugettext as _
from . import FakePage
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from aminbazar.model import DBSession, Product, SubCategory
from aminbazar.lib.base import BaseController


class ProductsController(BaseController):

    @expose('aminbazar.templates.products')
    def subcategory(self, sub_category_id):
        try:
            _id = int(sub_category_id)
        except ValueError:
            abort(404)
        products = DBSession.query(Product).filter(Product.sub_category_id == _id).all()
        if not products:
            abort(404)
        return dict(
            page=FakePage(header=u'محصولات دسته بندی %s' % products[0].sub_category.title),
            products=products
        )

    @expose('aminbazar.templates.product')
    def details(self, product_id):
        try:
            _id = int(product_id)
        except ValueError:
            abort(404)
        try:
            product = DBSession.query(Product).filter(Product.id == _id).one()
            return dict(
                page=FakePage(header=u'محصولات دسته بندی %s' % product.sub_category.title),
                product=product
            )
        except NoResultFound:
            abort(404)

    @expose('aminbazar.templates.new_product')
    def new(self):
        return dict(
            page=FakePage(u'افزودن کالای جدید'),
            sub_categories=DBSession.query(SubCategory).all()
        )

    @expose()
    def submit_product(self, **kwargs):
        if 'account_id' in session:
            try:
                product = Product(
                    title=kwargs['title'],
                    sub_category_id=kwargs['sub_category_id'],
                    year_of_production=kwargs['year_of_production'],
                    country_of_production=kwargs['country_of_production'],
                    quantity=kwargs['quantity'],
                    image=kwargs['image'],
                    price=kwargs['price'],
                    account_id=session.get('account_id', None)
                )
            except KeyError:
                abort(400)
            try:
                DBSession.add(product)
                DBSession.flush()
                return HTTPFound(location=lurl('/products/details/%s' % product.id))
            except IntegrityError:
                abort(400, detail=u'خطا در ثبت کالا. لطفا دوباره تلاش کنید')
        else:
            flash(u'برای ثبت کالا باید وارد سایت شوید', 'warning')
            return HTTPFound(location=lurl('/account/sign_in'))

    @expose()
    def remove_product(self, product_id):
        try:
            product = DBSession.query(Product).filter(Product.id == product_id).one()
        except NoResultFound:
            abort(404)
        if product.account.user_name == session.get('user_name', None):
            DBSession.delete(product)
            return HTTPFound(location=lurl('/'))
        else:
            abort(401)
