# -*- coding: utf-8 -*-

from tg import expose, abort, session, flash, lurl
from tg.decorators import paginate
from tg.exceptions import HTTPFound
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

    @expose('aminbazar.templates.my_products')
    @paginate('products', items_per_page=12)
    def my_products(self, acc_id):
        if 'user_name' in session:
            resp = dict()
            try:
                _id = int(acc_id)
            except ValueError:
                abort(404)
            products = DBSession.query(Product).filter(Product.account_id == _id)
            resp['page'] = FakePage(u'محصولات کاربر %s' % session['user_name'])
            resp['products'] = products
            if not products.all():
                resp['title'] = u'هنوز کالایی ثبت نشده است'
            else:
                resp['title'] = products[0].account.user_name
            return resp
        else:
            flash(u'برای مشاهده ی محصولاتی که ثبت کرده اید باید وارد سایت شوید', 'warning')
            return HTTPFound(location=lurl('/accounts/sign_in'))

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
            return HTTPFound(location=lurl('/accounts/sign_in'))

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
