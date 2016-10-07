# -*- coding: utf-8 -*-
from tgext.admin.controller import AdminController
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.config import CrudRestControllerConfig
from aminbazar import model
from .menu import ParentMenuAdminController, SubMenuAdminController
from .banner import BannerAdminController
from .stuff_history import BossHistoryAdminController, SecretaryHistoryAdminController
from .related_link import RelatedLinkAdminController, RelatedImageLinkAdminController
from .stuff import StuffAdminController
from .sponsor import SponsorAdminController
from .layout import CustomAdminLayout
from .social import SocialAdminController
from .product import ProductAdminController
from .category import CategoryAdminController
from .sub_category import SubCategoryAdminController
from .ad import AdAdminController
from .account import AccountAdminController


class LocalAdminConfig(TGAdminConfig):
    layout = CustomAdminLayout

    class parentmenu(CrudRestControllerConfig):
        defaultCrudRestController = ParentMenuAdminController

    class submenu(CrudRestControllerConfig):
        defaultCrudRestController = SubMenuAdminController

    class banner(CrudRestControllerConfig):
        defaultCrudRestController = BannerAdminController

    class account(CrudRestControllerConfig):
        defaultCrudRestController = AccountAdminController

    class product(CrudRestControllerConfig):
        defaultCrudRestController = ProductAdminController

    class category(CrudRestControllerConfig):
        defaultCrudRestController = CategoryAdminController

    class subcategory(CrudRestControllerConfig):
        defaultCrudRestController = SubCategoryAdminController

    class bosshistory(CrudRestControllerConfig):
        defaultCrudRestController = BossHistoryAdminController

    class secretaryhistory(CrudRestControllerConfig):
        defaultCrudRestController = SecretaryHistoryAdminController

    class relatedlink(CrudRestControllerConfig):
        defaultCrudRestController = RelatedLinkAdminController

    class relatedimagelink(CrudRestControllerConfig):
        defaultCrudRestController = RelatedImageLinkAdminController

    class stuff(CrudRestControllerConfig):
        defaultCrudRestController = StuffAdminController

    class sponsor(CrudRestControllerConfig):
        defaultCrudRestController = SponsorAdminController

    class social(CrudRestControllerConfig):
        defaultCrudRestController = SocialAdminController

    class ad(CrudRestControllerConfig):
        defaultCrudRestController = AdAdminController


class LocalAdminController(AdminController):
    def __init__(self, session):
        translations = {
            "user_id": "id",
            "group_id": "id",
         }

        super(LocalAdminController, self).__init__(
            [
                model.ParentMenu,
                model.SubMenu,
                model.Banner,
                model.BossHistory,
                model.SecretaryHistory,
                model.RelatedLink,
                model.RelatedImageLink,
                model.User,
                model.Group,
                model.Permission,
                model.Stuff,
                model.Account,
                model.Sponsor,
                model.Social,
                model.Category,
                model.SubCategory,
                model.Product,
                model.Ad,
            ],
            session,
            config_type=LocalAdminConfig,
            translations=translations)
