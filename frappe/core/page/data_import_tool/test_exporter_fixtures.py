# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
import frappe.defaults
from frappe.core.page.data_import_tool.data_import_tool import export_csv
import unittest

class TestDataImportFixtures(unittest.TestCase):
	
	def setUp(self):
		print "\nTeste for export explicit fixtures"
		print "see fixtures csv test files in sites folder"
	
	#start test for Custom Script
	def test_Custom_Script_fixture_simple(self):
		fixture = "Custom Script"
		path = frappe.scrub(fixture) + "_original_style.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Custom_Script_fixture_simple_name_equal_default(self):
		fixture = ["Custom Script", {"name":["Item-Client"]}]
		path = frappe.scrub(fixture[0]) + "_simple_name_equal_default.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Script_fixture_simple_name_equal(self):
		fixture = ["Custom Script", {"name":["Item-Client"],"op":"="}]
		path = frappe.scrub(fixture[0]) + "_simple_name_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Script_fixture_simple_name_not_equal(self):
		fixture = ["Custom Script", {"name":["Item-Client"],"op":"!="}]
		path = frappe.scrub(fixture[0]) + "_simple_name_not_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	#without [] around the name...
	def test_Custom_Script_fixture_simple_name_at_least_equal(self):
		fixture = ["Custom Script", {"name":"Item-Cli"}]
		path = frappe.scrub(fixture[0]) + "_simple_name_at_least_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Script_fixture_multi_name_equal(self):
		fixture = ["Custom Script", {"name":["Item-Client", "Customer-Client"],"op":"="}]
		path = frappe.scrub(fixture[0]) + "_multi_name_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Script_fixture_multi_name_not_equal(self):
		fixture = ["Custom Script", {"name":["Item-Client", "Customer-Client"],"op":"!="}]
		path = frappe.scrub(fixture[0]) + "_multi_name_not_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Custom_Script_fixture_empty_object(self):
		fixture = ["Custom Script", {}]
		path = frappe.scrub(fixture[0]) + "_empty_object_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Custom_Script_fixture_just_list(self):
		fixture = ["Custom Script"]
		path = frappe.scrub(fixture[0]) + "_just_list_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	# Custom Script regular expression
	def test_Custom_Script_fixture_rex_no_flags(self):
		fixture = ["Custom Script", {"name":r"^[i|A]"}]
		path = frappe.scrub(fixture[0]) + "_rex_no_flags.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Custom_Script_fixture_rex_with_flags(self):
		fixture = ["Custom Script", {"name":r"^[i|A]", "flags":"L,M"}]
		path = frappe.scrub(fixture[0]) + "_rex_with_flags.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
		
	#start test for Custom Field
	def test_Custom_Field_fixture_simple(self):
		fixture = "Custom Field"
		path = frappe.scrub(fixture) + "_original_style.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Custom_Field_fixture_simple_name_equal_default(self):
		fixture = ["Custom Field", {"name":["Item-vat"]}]
		path = frappe.scrub(fixture[0]) + "_simple_name_equal_default.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Field_fixture_simple_name_equal(self):
		fixture = ["Custom Field", {"name":["Item-vat"],"op":"="}]
		path = frappe.scrub(fixture[0]) + "_simple_name_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Field_fixture_simple_name_not_equal(self):
		fixture = ["Custom Field", {"name":["Item-vat"],"op":"!="}]
		path = frappe.scrub(fixture[0]) + "_simple_name_not_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	#without [] around the name...
	def test_Custom_Field_fixture_simple_name_at_least_equal(self):
		fixture = ["Custom Field", {"name":"Item-va"}]
		path = frappe.scrub(fixture[0]) + "_simple_name_at_least_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Custom_Field_fixture_multi_name_equal(self):
		fixture = ["Custom Field", {"name":["Item-vat", "Bin-vat"],"op":"="}]
		path = frappe.scrub(fixture[0]) + "_multi_name_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Field_fixture_multi_name_not_equal(self):
		fixture = ["Custom Field", {"name":["Item-vat", "Bin-vat"],"op":"!="}]
		path = frappe.scrub(fixture[0]) + "_multi_name_not_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Field_fixture_empty_object(self):
		fixture = ["Custom Field", {}]
		path = frappe.scrub(fixture[0]) + "_empty_object_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Custom_Field_fixture_just_list(self):
		fixture = ["Custom Field"]
		path = frappe.scrub(fixture[0]) + "_just_list_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	# Custom Field regular expression
	def test_Custom_Field_fixture_rex_no_flags(self):
		fixture = ["Custom Field", {"name":r"^[r|L]"}]
		path = frappe.scrub(fixture[0]) + "_rex_no_flags.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Custom_Field_fixture_rex_with_flags(self):
		fixture = ["Custom Field", {"name":r"^[i|A]", "flags":"L,M"}]
		path = frappe.scrub(fixture[0]) + "_rex_with_flags.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	
	#start test for Doctype
	def test_Doctype_fixture_simple(self):
		fixture = "ToDo"
		path = "Doctype_" + frappe.scrub(fixture) + "_original_style_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Doctype_fixture_simple_name_equal_default(self):
		fixture = ["ToDo", {"name":["TDI00000008"]}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_simple_name_equal_default.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Doctype_fixture_simple_name_equal(self):
		fixture = ["ToDo", {"name":["TDI00000002"],"op":"="}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_simple_name_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Doctype_simple_name_not_equal(self):
		fixture = ["ToDo", {"name":["TDI00000002"],"op":"!="}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_simple_name_not_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	#without [] around the name...
	def test_Doctype_fixture_simple_name_at_least_equal(self):
		fixture = ["ToDo", {"name":"TDI"}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_simple_name_at_least_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Doctype_multi_name_equal(self):
		fixture = ["ToDo", {"name":["TDI00000002", "TDI00000008"],"op":"="}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_multi_name_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	def test_Doctype_multi_name_not_equal(self):
		fixture = ["ToDo", {"name":["TDI00000002", "TDI00000008"],"op":"!="}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_multi_name_not_equal.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Doctype_fixture_empty_object(self):
		fixture = ["ToDo", {}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_empty_object_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Doctype_fixture_just_list(self):
		fixture = ["ToDo"]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_just_list_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	# Doctype regular expression
	def test_Doctype_fixture_rex_no_flags(self):
		fixture = ["ToDo", {"name":r"^TDi"}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_rex_no_flags_should_be_all.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
		
	def test_Doctype_fixture_rex_with_flags(self):
		fixture = ["ToDo", {"name":r"^TDi", "flags":"L,M"}]
		path = "Doctype_" + frappe.scrub(fixture[0]) + "_rex_with_flags_should_be_none.csv"
		print "teste done {}".format(path)
		export_csv(fixture, path)
		self.assertTrue(True)
	
	