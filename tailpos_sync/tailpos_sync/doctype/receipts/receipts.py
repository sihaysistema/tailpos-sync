# -*- coding: utf-8 -*-
# Copyright (c) 2018, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from tailpos_sync.utils import set_date_updated

import uuid


class Receipts(Document):
	def autoname(self):
		if not self.id:
			self.id = 'Receipt/' + str(uuid.uuid4())
		self.name = self.id

	def validate(self):
		set_date_updated(self)

	def set_total_amount(self):
		self.total_amount = 0

	def set_default_values(self):
		"""Set the status as title-d form"""
		self.status = self.status.title()
		self.series = 'Receipt/{0}'.format(self.receiptnumber)
		self.set_total_amount()

	def before_insert(self):
		"""Setup the Receipts document"""
		self.set_default_values()
