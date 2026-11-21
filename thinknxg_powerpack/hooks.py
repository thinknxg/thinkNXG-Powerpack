app_name = "thinknxg_powerpack"
app_title = "thinkNXG PowerPack"
app_publisher = "thinkNXG"
app_description = "Custom thinkNXG app for thinkNXG PowerPack features"
app_email = "support@thinknxg.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "thinknxg_powerpack",
# 		"logo": "/assets/thinknxg_powerpack/logo.png",
# 		"title": "thinkNXG PowerPack",
# 		"route": "/thinknxg_powerpack",
# 		"has_permission": "thinknxg_powerpack.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
#
# These are BARE BUNDLE NAMES, not /assets/... paths, and that distinction matters.
# thinkNXG resolves a name containing ".bundle." through assets.json to a
# content-hashed file (bundled_asset(), frappe/utils/jinja_globals.py:147); a
# literal /assets path is served verbatim, with no hash and no ?ver=, so browsers
# cache it indefinitely and deployed changes never reach anyone who does not
# manually hard-reload. The individual source files are imported, in order, by the
# two bundle entry points. The CSS entry is authored as .scss (so sass can
# resolve its sibling imports) but esbuild emits .css, and assets.json is keyed
# by the OUTPUT name -- hence ".bundle.css" here, same as erpnext.
app_include_css = "thinknxg_powerpack.bundle.css"
app_include_js = "thinknxg_powerpack.bundle.js"

# include js, css files in header of web template
# web_include_css = "/assets/thinknxg_powerpack/css/thinknxg_powerpack.css"
# web_include_js = "/assets/thinknxg_powerpack/js/thinknxg_powerpack.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "thinknxg_powerpack/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Payment Entry": [
        "public/js/kenya_withholding_payment_entry.js",
    ],
    "Journal Entry": [
        "public/js/kenya_withholding_journal_entry.js",
    ],
    "Sales Order": [
        "public/js/quick_pay.js",
        "public/js/quick_pay_mpesa.js",
    ],
    "Email Group": [
        "public/js/email_group_powerup.js",
    ],
    "Email Queue": [
        "public/js/email_queue_preview.js",
    ],
}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "thinknxg_powerpack/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Website Route Rules
# -------------------
website_route_rules = [
	# path: tokens minted before build_public_link cleaned names can contain "/"
	# (LPO/26/09/00109-Fq0R); the default converter stops at the first one.
	{"from_route": "/s/<path:token>", "to_route": "s"},
]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
	"methods": [
		"thinknxg_powerpack.jinja.get_document_public_link",
		"thinknxg_powerpack.barcode.qr_data_uri",
	],
}

# Installation
# ------------

# before_install = "thinknxg_powerpack.install.before_install"
after_install = [
    "thinknxg_powerpack.price_approval.setup_custom_fields",
    "thinknxg_powerpack.copy_as_message.seed_client_scripts",
    "thinknxg_powerpack.kenya_withholding.setup_custom_fields",
    "thinknxg_powerpack.pos_list_floor.setup_custom_fields",
]
after_migrate = [
    "thinknxg_powerpack.price_approval.after_migrate",
    "thinknxg_powerpack.kenya_withholding.setup_custom_fields",
    "thinknxg_powerpack.copy_as_message.seed_client_scripts",
    "thinknxg_powerpack.branch_naming.after_migrate",
    "thinknxg_powerpack.pos_list_floor.setup_custom_fields",
]

# Naming-series placeholders (.CO. .BR. .SET. .PAYDIR. .ST. .RET.), the hook thinkNXG ERP uses for .ABBR.
naming_series_variables = {
    v: "thinknxg_powerpack.branch_naming.parse_variable"
    for v in ("CO", "CO/", "CO-", "CO_", "BR", "BR/", "BR-", "BR_", "SET", "SET/", "SET-", "SET_", "PAYDIR", "RET", "RET/", "RET-", "RET_", "ST", "ST/", "ST-", "ST_")
}

# Fixtures
# --------

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Quotation-set_warehouse"
                ]
            ]
        ]
    },
    {
        "dt": "Server Script",
        "filters": [
            ["module", "in", ["thinkNXG PowerPack"]]
        ]
    },
    {
        "dt": "Client Script",
        "filters": [
            ["module", "in", ["thinkNXG PowerPack"]]
        ]
    }
]

# Uninstallation
# ------------

# before_uninstall = "thinknxg_powerpack.uninstall.before_uninstall"
# after_uninstall = "thinknxg_powerpack.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "thinknxg_powerpack.utils.before_app_install"
# after_app_install = "thinknxg_powerpack.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "thinknxg_powerpack.utils.before_app_uninstall"
# after_app_uninstall = "thinknxg_powerpack.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "thinknxg_powerpack.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Extend standard doctype classes (v16+). Layers our mixin on top of thinkNXG ERP's
# controller instead of replacing it, so upstream fixes are preserved and other
# apps extending the same doctype are not clobbered.

extend_doctype_class = {
	"Payment Reconciliation": "thinknxg_powerpack.custom_payment_reconciliation.CustomPaymentReconciliation"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"User": {
		"validate": "thinknxg_powerpack.pos_supervisor_pin.validate_pin_format",
	},
	"Quotation": {
		"before_validate": "thinknxg_powerpack.price_approval.guard_pending_edit",
		"validate": "thinknxg_powerpack.min_selling_price.validate_min_selling_price",
		"on_update": "thinknxg_powerpack.price_approval.stamp_price_approval",
	},
	"Sales Order": {
		"before_validate": "thinknxg_powerpack.price_approval.guard_pending_edit",
		"validate": "thinknxg_powerpack.min_selling_price.validate_min_selling_price",
		"on_update": "thinknxg_powerpack.price_approval.stamp_price_approval",
	},
	"Sales Invoice": {
		"before_validate": "thinknxg_powerpack.price_approval.guard_pending_edit",
		"before_cancel": "thinknxg_powerpack.validations.prevent_etr_invoice_cancellation",
		"validate": [
			"thinknxg_powerpack.min_selling_price.validate_min_selling_price",
			# A return keeps the original sale's tax_id (validations.py).
			"thinknxg_powerpack.validations.carry_return_tax_id",
		],
		"on_update": "thinknxg_powerpack.price_approval.stamp_price_approval",
	},
	"POS Invoice": {
		"before_cancel": "thinknxg_powerpack.validations.prevent_etr_invoice_cancellation",
		"validate": "thinknxg_powerpack.min_selling_price.validate_min_selling_price"
	},
	"Delivery Note": {
		"before_validate": "thinknxg_powerpack.price_approval.guard_pending_edit",
		"validate": "thinknxg_powerpack.min_selling_price.validate_min_selling_price",
		"on_update": "thinknxg_powerpack.price_approval.stamp_price_approval",
	},
	"Payment Reconciliation": {
		"validate": "thinknxg_powerpack.overrides.validate_allocation_with_zero_support"
	},
	"Payment Entry": {
		"before_validate": "thinknxg_powerpack.kenya_withholding.apply_to_payment_entry",
		"before_update_after_submit": "thinknxg_powerpack.kenya_withholding.link_deposit_rows",
		"before_cancel": "thinknxg_powerpack.kenya_withholding.prevent_cancel_if_paid_to_kra",
	},
	"Purchase Invoice": {
		"before_cancel": "thinknxg_powerpack.kenya_withholding.refuse_cancel_if_deposit_paid_to_kra",
		"on_cancel": "thinknxg_powerpack.kenya_withholding.unlink_deposit_rows",
	},
	"Unreconcile Payment": {
		"before_submit": "thinknxg_powerpack.kenya_withholding.refuse_unreconcile_if_deposit_paid_to_kra",
		"on_submit": "thinknxg_powerpack.kenya_withholding.unlink_deposit_rows_on_unreconcile",
	},
	"Journal Entry": {
		"onload": "thinknxg_powerpack.kenya_withholding.flag_kra_payment",
		"before_insert": "thinknxg_powerpack.kenya_withholding.refuse_kra_amend",
		"before_cancel": "thinknxg_powerpack.kenya_withholding.allow_cancel_of_kra_payment",
		"on_cancel": "thinknxg_powerpack.kenya_withholding.clear_kra_link",
	},
	"Workflow": {
		"before_validate": "thinknxg_powerpack.price_approval.guard_managed_workflow",
		"validate": "thinknxg_powerpack.price_approval.guard_managed_workflow",
		"on_trash": "thinknxg_powerpack.price_approval.guard_managed_workflow",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"thinknxg_powerpack.tasks.all"
# 	],
# 	"daily": [
# 		"thinknxg_powerpack.tasks.daily"
# 	],
# 	"hourly": [
# 		"thinknxg_powerpack.tasks.hourly"
# 	],
# 	"weekly": [
# 		"thinknxg_powerpack.tasks.weekly"
# 	],
# 	"monthly": [
# 		"thinknxg_powerpack.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "thinknxg_powerpack.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	# search_link is the actual HTTP endpoint the Link field calls.
	# search_link → search_widget → frappe.call(query) all happen in Python, bypassing
	# handler.py's override_whitelisted_methods lookup. Overriding search_link lets us
	# substitute custom_item_query before the chain runs.
	"frappe.desk.search.search_link": "thinknxg_powerpack.api.custom_search_link",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other thinkNXG apps
# override_doctype_dashboards = {
# 	"Task": "thinknxg_powerpack.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["thinknxg_powerpack.utils.before_request"]
# after_request = ["thinknxg_powerpack.utils.after_request"]

# Job Events
# ----------
# before_job = ["thinknxg_powerpack.utils.before_job"]
# after_job = ["thinknxg_powerpack.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"thinknxg_powerpack.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

