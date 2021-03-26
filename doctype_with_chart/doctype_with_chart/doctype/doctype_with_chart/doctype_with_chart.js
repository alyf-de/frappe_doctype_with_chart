// Copyright (c) 2021, ALYF GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('DocType With Chart', {
	refresh: function(frm) {
		$(frm.fields_dict['chart'].wrapper)
			.html(frappe.render_template('my_chart'));
	}
});
