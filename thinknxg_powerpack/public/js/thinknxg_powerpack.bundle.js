/**
 * Desk JS bundle for thinkNXG PowerPack.
 *
 * Referenced by hooks.py as `app_include_js = "thinknxg_powerpack.bundle.js"` (a bare
 * bundle name, NOT an /assets path). thinkNXG resolves bare bundle names through
 * assets.json to a content-hashed filename -- see bundled_asset() in
 * frappe/utils/jinja_globals.py. That hash is the whole point: the previous
 * /assets/... paths carried no hash and no ?ver=, so browsers cached them forever
 * and shipped changes stayed invisible until each user happened to hard-reload.
 *
 * Import order is load order, and it matches the old app_include_js list exactly.
 * thinknxg_powerpack.js MUST come first: it defines window.thinkNXGPowerPack, which
 * every other file uses.
 *
 * Note: esbuild gives each file its own module scope, so top-level declarations are
 * no longer global. Anything shared between files must go on window.thinkNXGPowerPack
 * or a frappe.provide() namespace, as thinkNXGPowerPack.formatNumber now does.
 */

import "./thinknxg_powerpack.js";
import "./profit_calculator.js";
import "./sales_powerup.js";
import "./bulk_selection.js";
import "./payment_reconciliation_powerup.js";
import "./lens_powerup.js";
import "./price_import_powerup.js";
import "./copy_as_image.js";
import "./rate_price_picker.js";
