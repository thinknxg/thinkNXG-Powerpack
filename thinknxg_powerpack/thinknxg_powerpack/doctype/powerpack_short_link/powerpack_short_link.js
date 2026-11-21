// Copyright (c) 2026, thinkNXG and contributors
// For license information, please see license.txt

frappe.ui.form.on('PowerPack Short Link', {
	refresh: function (frm) {
		thinknxg_render_short_url(frm);
	},
});

function thinknxg_get_short_url(frm) {
	const token = frm.doc.token || frm.doc.name;
	if (!token) {
		return null;
	}
	const path = '/s/' + encodeURIComponent(token);
	return { path: path, url: frappe.urllib.get_base_url() + path };
}

function thinknxg_render_short_url(frm) {
	// The sidebar is hidden until the document is saved
	if (frm.is_new()) {
		return;
	}

	const link = thinknxg_get_short_url(frm);
	if (!link) {
		return;
	}

	const sidebar = frm.sidebar && frm.sidebar.sidebar;
	const anchor = sidebar && sidebar.find('.sidebar-meta-details .ellipsis').first();

	if (!anchor || !anchor.length) {
		// thinkNXG changed the sidebar markup — keep the link reachable anyway
		frm.add_custom_button(__('Copy Link'), function () {
			frappe.utils.copy_to_clipboard(link.url);
		});
		return;
	}

	anchor.find('.thinknxg-short-url').remove();

	const row = $(`
		<div class="thinknxg-short-url mt-1 flex justify-between">
			<a class="thinknxg-short-url-open ellipsis mr-2" target="_blank" rel="noopener noreferrer">
				${frappe.utils.icon('es-line-link', 'sm')}
				<span class="thinknxg-short-url-text"></span>
			</a>
			<a class="thinknxg-short-url-copy" href="#">
				${frappe.utils.icon('es-line-copy-light', 'sm')}
			</a>
		</div>
	`);

	row.attr('title', link.url);
	row.find('.thinknxg-short-url-open').attr('href', link.url);
	row.find('.thinknxg-short-url-text').text(link.path);
	row.find('.thinknxg-short-url-copy')
		.attr('title', __('Copy short link'))
		.on('click', function (e) {
			e.preventDefault();
			frappe.utils.copy_to_clipboard(link.url);
		});

	anchor.append(row);
}
