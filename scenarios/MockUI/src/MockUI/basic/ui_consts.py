"""UI constants for the new Specter DIY clean interface."""
from micropython import const
import lvgl as lv

# --- Screen dimensions ---
SCREEN_WIDTH = const(480)
SCREEN_HEIGHT = const(800)

# --- Layout zone heights (pixels) ---
TOP_BAR_HEIGHT = const(56)
SEED_DROPDOWN_HEIGHT = const(52)
NAV_BAR_HEIGHT = const(56)

# Wallet section: fits ~3 wallet rows (bigger rows + more spacing between them)
WALLET_SECTION_HEIGHT = const(260)

# Action buttons fill remaining space
# 800 - 56 - 52 - 260 - 56 = 376px for action area

# --- Button sizes ---
# Sized so Scan + Receive + SD Card always fit the dashboard action area
# without scrolling/clipping (see _DASHBOARD_H in specter_gui.py).
BTN_SMALL_HEIGHT = const(80)        # SD Card
BTN_MED_HEIGHT = const(92)          # Receive (below Scan, a notch smaller)
BTN_LARGE_HEIGHT = const(140)       # Scan button (largest, centered)
BTN_RADIUS = const(16)

# --- Wallet row ---
WALLET_ROW_HEIGHT = const(64)
WALLET_ROW_HEIGHT_ACTIVE = const(78)
WALLET_ICON_SIZE = const(20)

# --- Standard list/nav row (used across settings, seed menu, wallet menu, etc.) ---
ROW_HEIGHT = const(60)
ROW_ICON_ZOOM = const(170)

# --- Bottom nav ---
NAV_BTN_SIZE = const(44)

# --- Font sizes ---
FONT_TITLE = const(22)
FONT_BODY = const(16)
FONT_SMALL = const(12)
FONT_ICON = const(22)

# --- Spacing ---
PAD_XS = const(4)
PAD_SM = const(8)
PAD_MD = const(12)
PAD_LG = const(16)
PAD_XL = const(24)

# --- Icon sizes ---
BTC_ICON_WIDTH = const(42)
BTC_ICON_ZOOM = const(256)
ICON_SM = const(20)
ICON_MD = const(28)
ICON_LG = const(42)

# --- Status bar (legacy compat for Battery stub) ---
STATUS_BTN_HEIGHT = const(40)
STATUS_BTN_WIDTH = const(50)

# --- Modal ---
MODAL_WIDTH_PCT = const(85)
MODAL_HEIGHT_PCT = const(80)

# --- PIN ---
PIN_BTN_HEIGHT = const(85)
PIN_BTN_WIDTH = const(115)

# --- Keyboard manager compat ---
SWITCH_HEIGHT = const(82)
SWITCH_WIDTH = const(45)
BTN_HEIGHT = const(75)
BTN_WIDTH = const(100)
MENU_PCT = const(100)
PAD_SIZE = const(5)
ONE_LETTER_SYMBOL_WIDTH = const(16)
TWO_LETTER_SYMBOL_WIDTH = const(28)
THREE_LETTER_SYMBOL_WIDTH = const(40)
MENU_TITLE_FONT_SIZE = const(22)
MENU_ITEM_FONT_SIZE = const(16)
STATUS_BAR_PCT = const(5)
CONTENT_PCT = const(90)
BACK_BTN_HEIGHT = const(70)
BACK_BTN_WIDTH = const(48)
TITLE_ROW_HEIGHT = const(60)
TITLE_PADDING = const(15)
EXPLAINER_WIDTH_PCT = const(70)
EXPLAINER_HEIGHT_PCT = const(40)
EXPLAINER_OVERLAY_OPA = const(200)

# === COLOR SCHEME — "Specter" theme, ported from the palette in
# k9ert/specter-playground PR #35 (specter_ui_theme_specter.json v1.1):
# navy canvas, single blue accent, teal/amber/coral semantics. ===

# Primary (PR35 PRIMARY / SECONDARY — same blue for both)
CYAN = "#1F99E5"
CYAN_HEX = lv.color_hex(0x1F99E5)
CYAN_DARK = "#1773AC"          # darkened PRIMARY, for pressed states/borders
CYAN_DARK_HEX = lv.color_hex(0x1773AC)

# Backgrounds (PR35 CANVAS / QUATERNARY)
BG_BLACK = "#081A2A"           # CANVAS
BG_BLACK_HEX = lv.color_hex(0x081A2A)
BG_DARK = "#081A2A"            # CANVAS (theme's BG.DARK also maps to CANVAS)
BG_DARK_HEX = lv.color_hex(0x081A2A)
BG_CARD = "#24384C"            # QUATERNARY
BG_CARD_HEX = lv.color_hex(0x24384C)
BG_ELEVATED = "#2E4864"        # lightened QUATERNARY, for active/selected rows
BG_ELEVATED_HEX = lv.color_hex(0x2E4864)

# Text (PR35 INK / NEUTRAL)
WHITE = "#F5F8FC"              # INK
WHITE_HEX = lv.color_hex(0xF5F8FC)
GREY_LIGHT = "#7D91A5"         # NEUTRAL
GREY_LIGHT_HEX = lv.color_hex(0x7D91A5)
GREY = "#5C6E80"               # darkened NEUTRAL
GREY_HEX = lv.color_hex(0x5C6E80)
GREY_DARK = "#3A4E63"          # between QUATERNARY and NEUTRAL, for dividers
GREY_DARK_HEX = lv.color_hex(0x3A4E63)

# Semantic (PR35 SUCCESS / WARNING / DANGER)
GREEN = "#31D39A"
GREEN_HEX = lv.color_hex(0x31D39A)
ORANGE = "#F5B84B"
ORANGE_HEX = lv.color_hex(0xF5B84B)
RED = "#FF6878"
RED_HEX = lv.color_hex(0xFF6878)
YELLOW = "#F5B84B"             # theme has no separate yellow; alias to WARNING
YELLOW_HEX = lv.color_hex(0xF5B84B)

BLACK = "#000000"
BLACK_HEX = lv.color_hex(0x000000)

# Warning background (subtle amber tint for address reuse, security warnings)
BG_WARN = "#332912"
BG_WARN_HEX = lv.color_hex(0x332912)
