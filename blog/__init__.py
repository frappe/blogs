__version__ = "0.0.1"
import frappe
from frappe.utils.modules import get_modules_from_all_apps_for_user


def check_app_permission():
	if frappe.session.user == "Administrator":
		return True

	allowed_modules = get_modules_from_all_apps_for_user()
	allowed_modules = [x["module_name"] for x in allowed_modules]
	if "Blog" not in allowed_modules:
		return False

	roles = frappe.get_roles()
	if any(role in ["Blogger"] for role in roles):
		return True

	return False
