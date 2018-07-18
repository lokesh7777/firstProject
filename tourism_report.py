# Copyright (c) 2013, lokesh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = get_colums(filters)
	data = get_data(filters)
	return columns, data

def get_data(filters):
	# query_data = get_query_condition(filters)
	data = frappe.db.sql("""
	select 
		rg.salutation,rg.first_name,rg.last_name,rg.gender,rg.date_of_birth,rg.country,rg.state,rg.city,rg.email,rg.mobile_no,rg.language_preferred 
	from
		`tabRegistration` as rg
	where 
			{0}"""
		.format(get_conditions(filters)),debug = 1)

	return data

def get_conditions(filters):
	conditions = ''
	if filters.country:
		conditions += "rg.country = '{0}'".format(filters.country)
		print "\n\n conditions ====",conditions
	if filters.first_name:
	 	conditions += " and rg.first_name = '{0}'".format(filters.first_name)
	 	print "\n\n conditions ====",conditions
	if filters.last_name:
		conditions += "and rg.last_name = '{0}'".format(filters.last_name)
		print "\n\n conditions ====",conditions
	if filters.city:
		conditions += "and rg.city = '{0}'".format(filters.city)
		print "\n\n conditions ====",conditions
	return conditions	

def get_colums(filters):
	columns = [ ("Salutation") + ":Select:100",
	("First Name") + ":Data:100",
	("Last Name") + ":Data:100",
	("Gender") + ":Select:100",
	("Date Of Birth") + ":Date:100",
	("Country") + ":Link/Country:100",
	("State") + ":Select:100",
	("City") + ":Data:100",
	("Email") + ":Data:100",
	("Mobile No") + ":Data:100",
	("Language Preffered") + ":Link/Language:100",
	]
	return columns
