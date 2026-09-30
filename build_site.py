"""Builds the Car Tow Jam: Parking Puzzle website (GitHub Pages): home (marketing + QR), privacy policy, terms of use,
support, the QR/download redirect and app-ads.txt. Edit the constants below, run `python3 build_site.py`, commit, push.
"""
from pathlib import Path
ROOT = Path(__file__).parent
GAME = "Car Tow Jam: Parking Puzzle"
DEVELOPER = "Kinex Apps"
DEV_SITE = "https://kinexapps.com/"
EMAIL = "muhammadharisgift1@gmail.com"
BASE = "https://mu-haris.github.io/Car-Tow-Jam-Parking-Puzzle/"
# Paste the App Store link here once the app is live (e.g. https://apps.apple.com/app/id1234567890), then rebuild.
# The QR code points at /download/, which forwards here, so the printed QR code never needs to change.
APP_STORE_URL = ""
PRICE = "$3.99"
UPDATED = "September 30, 2026"

CSS = """
:root{--teal:#0D838F;--teal-d:#0A4F57;--cream:#FFF6E4;--card:#FFFFFF;--ink:#2B1B10;--muted:#6B5646;--yellow:#FFC526;--red:#E8452C;--line:#EAD9BD;--bg:#FFF1D6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--cream:#0F2A2E;--card:#15373C;--ink:#F4ECDD;--muted:#BFD3D0;--line:#24545A;--bg:#0B2226}}
:root[data-theme="dark"]{--cream:#0F2A2E;--card:#15373C;--ink:#F4ECDD;--muted:#BFD3D0;--line:#24545A;--bg:#0B2226}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 "Nunito",system-ui,-apple-system,Segoe UI,sans-serif}
a{color:var(--teal);font-weight:700}@media (prefers-color-scheme:dark){a{color:#5FD4DE}}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header.top{background:var(--teal);color:#fff}
header.top .wrap{display:flex;align-items:center;gap:12px;min-height:64px;flex-wrap:wrap}
header.top a.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font:600 20px "Fredoka",sans-serif}
header.top img{width:36px;height:36px;border-radius:9px}
header.top nav{margin-left:auto;display:flex;gap:16px;flex-wrap:wrap}
header.top nav a{color:#E6FAFB;font-weight:700;text-decoration:none;font-size:15px}
header.top nav a:hover{color:#fff;text-decoration:underline}
h1,h2,h3{font-family:"Fredoka",sans-serif;line-height:1.2}
h1{font-size:clamp(32px,6vw,52px);margin:.2em 0}h2{font-size:28px;margin:1.6em 0 .4em}h3{font-size:20px;margin:1.3em 0 .3em}
.hero{background:linear-gradient(180deg,var(--teal) 0,#12959F 100%);color:#fff;padding:48px 0 64px}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:36px;align-items:center}
.hero p.lead{font-size:20px;color:#E9FBFC;max-width:34em}
.hero img.logo{width:100%;max-width:420px;display:block;margin:0 auto;filter:drop-shadow(0 18px 30px rgba(0,0,0,.25))}
.btn{display:inline-flex;align-items:center;gap:10px;background:#111;color:#fff;border-radius:14px;padding:12px 22px;text-decoration:none;font:600 18px "Fredoka",sans-serif;box-shadow:0 6px 0 rgba(0,0,0,.25)}
.btn small{display:block;font:500 12px "Nunito",sans-serif;opacity:.85}
.btn svg{width:28px;height:28px;fill:#fff}
.qr{display:flex;gap:18px;align-items:center;margin-top:26px;background:rgba(255,255,255,.12);border-radius:18px;padding:14px;max-width:420px}
.qr img{width:128px;height:128px;border-radius:12px;background:#fff}
.qr p{margin:0;color:#fff;font-size:15px}
section{padding:40px 0}
.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.card{background:var(--card);border:2px solid var(--line);border-radius:20px;padding:20px}
.card h3{margin-top:0}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.shots img{width:100%;border-radius:22px;border:4px solid #fff;box-shadow:0 10px 24px rgba(0,0,0,.18)}
.doc{background:var(--card);border:2px solid var(--line);border-radius:24px;padding:28px clamp(18px,4vw,44px);margin:32px auto 48px;max-width:860px}
.doc p,.doc li{color:var(--ink)}.doc .meta{color:var(--muted);margin-top:0}
.faq details{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:14px 18px;margin:10px 0}
.faq summary{cursor:pointer;font:600 18px "Fredoka",sans-serif}
.contact{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
footer{background:var(--teal-d);color:#D6F1F3;padding:26px 0;font-size:14px}
footer .wrap{display:flex;flex-wrap:wrap;gap:14px 22px;align-items:center}
footer a{color:#fff;font-weight:600}
@media (max-width:760px){.hero .wrap{grid-template-columns:1fr}.hero{padding:32px 0 44px}.shots{grid-template-columns:1fr 1fr}.shots img:nth-child(3){display:none}.qr img{width:104px;height:104px}}
"""

APPLE = '<svg viewBox="0 0 384 512" aria-hidden="true"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>'

def page(title, body, path, description, depth=1):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{up}assets/favicon.png">
<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{BASE}assets/icon-512.png">
<meta property="og:url" content="{BASE}{path}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{up}"><img src="{up}assets/icon-512.png" alt=""><span>Car Tow Jam</span></a>
<nav><a href="{up}">Home</a><a href="{up}support/">Support</a><a href="{up}privacy/">Privacy</a><a href="{up}terms/">Terms</a></nav>
</div></header>
{body}
<footer><div class="wrap">
<span>&copy; 2026 {DEVELOPER}</span>
<a href="{up}privacy/">Privacy Policy</a><a href="{up}terms/">Terms of Use</a><a href="{up}support/">Support</a>
<a href="mailto:{EMAIL}">{EMAIL}</a><a href="{DEV_SITE}">kinexapps.com</a>
</div></footer>
</body>
</html>
"""

def write(rel, html):
    p = ROOT / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(html)

store_button = f'<a class="btn" href="download/">{APPLE}<span><small>Download on the</small>App Store</span></a>'

home = f"""
<section class="hero"><div class="wrap">
<div>
<h1>{GAME}</h1>
<p class="lead">Untangle the traffic jam! Tap cars in the right order, send them onto matching tow trucks and ferries, and keep the spare parking spots free. A relaxing, colourful puzzle across a tropical harbor, snowy docks and an autumn lake.</p>
{store_button}
<div class="qr"><img src="assets/qr-app-store-small.png" alt="QR code that opens Car Tow Jam on the App Store"><p><strong>Scan to download</strong><br>Point your iPhone camera at the code to open Car Tow Jam on the App Store.</p></div>
</div>
<img class="logo" src="assets/logo.png" alt="Car Tow Jam: Parking Puzzle logo">
</div></section>
<section><div class="wrap">
<h2>Screenshots</h2>
<div class="shots">
<img src="assets/screen-1.jpg" alt="Tropical harbor level with tow trucks and a ferry" loading="lazy">
<img src="assets/screen-2.jpg" alt="Snowy harbor level with falling snow" loading="lazy">
<img src="assets/screen-3.jpg" alt="Autumn lake level with falling leaves" loading="lazy">
</div>
<h2>Why players love it</h2>
<div class="features">
<div class="card"><h3>Tow &amp; ferry puzzles</h3><p>Flatbeds, cranes, wreckers and heavy tow trucks each lift different cars, while ferries carry six at a time.</p></div>
<div class="card"><h3>Endless levels</h3><p>Hand-tuned, always-solvable puzzles that keep going: when you finish the last level, a new round begins.</p></div>
<div class="card"><h3>Three living maps</h3><p>A tropical harbor, a snowy port and an autumn lake, with fishing boats, a cargo helicopter and ducks.</p></div>
<div class="card"><h3>Coins &amp; shop</h3><p>Earn coins for every level and unlock special tow trucks and ferries in the shop.</p></div>
</div>
</div></section>
"""
write("index.html", page(GAME, home, "", "Car Tow Jam: Parking Puzzle, a relaxing traffic puzzle game for iPhone and iPad.", depth=0).replace('href="../','href="').replace('src="../','src="'))

privacy = f"""
<main class="wrap"><article class="doc">
<h1>Privacy Policy</h1>
<p class="meta">{GAME} &middot; Last updated {UPDATED}</p>
<p>This policy explains what information is used when you play {GAME} (the "App"), published by {DEVELOPER} ("we", "us"). If you have questions, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Information we collect</h2>
<p>We do not ask for your name, email, contacts or location, and we do not run our own servers that collect data about you. The App stores your game progress, coins, shop items and settings <strong>only on your device</strong>. Deleting the App deletes this data.</p>
<p>We do not use analytics services in the App.</p>
<h2>Advertising (Google AdMob)</h2>
<p>Free players see ads, which are provided by Google AdMob. To show, limit and measure ads and to prevent fraud, Google may collect information from your device such as the advertising identifier (IDFA), IP address, device and app information, approximate location derived from the IP address, and how you interact with ads.</p>
<ul>
<li><strong>App Tracking Transparency:</strong> on iOS, the App asks for permission before the advertising identifier can be used for tracking. If you choose "Ask App Not to Track", ads are still shown but are not personalised with that identifier. You can change this at any time in <em>Settings &gt; Privacy &amp; Security &gt; Tracking</em>.</li>
<li><strong>Consent (EEA, UK and Switzerland):</strong> where required by law, the App shows Google's consent message before any personalised ads are served, and you can choose your preferences.</li>
</ul>
<p>Learn more in Google's policies: <a href="https://policies.google.com/technologies/ads">How Google uses information in ads</a> and <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a>.</p>
<h2>Purchases</h2>
<p>Premium subscriptions are purchased through Apple's App Store. Apple processes the payment; we never see or store your payment details. The App only receives confirmation from Apple that a purchase is active so it can remove ads.</p>
<h2>Children</h2>
<p>The App is not directed to children under 13, and we do not knowingly collect personal information from children. If you believe a child has provided personal information, contact us and we will help remove it.</p>
<h2>Your choices</h2>
<ul>
<li>Turn off ad tracking in iOS Settings, or reset your advertising identifier.</li>
<li>Remove banner ads and ads between levels with a Premium subscription.</li>
<li>Delete the App to remove all game data stored on your device.</li>
</ul>
<h2>Data retention and security</h2>
<p>Because game data stays on your device, we do not retain it. Information collected by Google for advertising is handled under Google's privacy policy.</p>
<h2>Changes to this policy</h2>
<p>We may update this policy from time to time. The "Last updated" date above shows when it last changed.</p>
<h2>Contact</h2>
<p>{DEVELOPER} &middot; <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="{DEV_SITE}">{DEV_SITE}</a></p>
</article></main>
"""
write("privacy/index.html", page(f"Privacy Policy | {GAME}", privacy, "privacy/", f"Privacy policy for {GAME}."))

terms = f"""
<main class="wrap"><article class="doc">
<h1>Terms of Use</h1>
<p class="meta">{GAME} &middot; Last updated {UPDATED}</p>
<p>These Terms of Use govern your use of {GAME} (the "App") published by {DEVELOPER}. By downloading or playing the App you agree to these terms and to Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard Licensed Application End User License Agreement</a>, which also applies.</p>
<h2>License</h2>
<p>We grant you a personal, non-transferable, non-exclusive license to use the App on Apple devices you own or control, as permitted by the App Store terms.</p>
<h2>Premium subscription</h2>
<ul>
<li><strong>Premium</strong> is an auto-renewing monthly subscription ({PRICE} per month in the US; the price in your local currency is shown in the App before you buy). It removes banner ads and the ads shown between levels. Optional rewarded videos (for example, doubling coins) remain available.</li>
<li>Payment is charged to your Apple ID account when you confirm the purchase.</li>
<li>The subscription renews automatically unless it is cancelled at least 24 hours before the end of the current period. Your account is charged for renewal within 24 hours before the end of the current period.</li>
<li>You can manage or cancel your subscription in your Apple ID account settings (<em>Settings &gt; [your name] &gt; Subscriptions</em>). Deleting the App does not cancel the subscription.</li>
<li>Refunds are handled by Apple under its policies. You can request one at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
<li>If you reinstall the App or use a new device, tap <strong>Restore Purchases</strong> in the App to restore Premium.</li>
</ul>
<h2>Virtual coins and items</h2>
<p>Coins and shop items (such as special tow trucks and ferries) are earned in the game, have no real-world monetary value, cannot be exchanged for money, and are stored on your device.</p>
<h2>Advertising</h2>
<p>The free version of the App shows ads provided by third parties. See our <a href="../privacy/">Privacy Policy</a> for details.</p>
<h2>Acceptable use</h2>
<p>Do not reverse engineer, modify, or use the App for any unlawful purpose, or attempt to interfere with its purchases or advertising.</p>
<h2>Disclaimer and limitation of liability</h2>
<p>The App is provided "as is" without warranties of any kind, to the extent permitted by law. To the maximum extent permitted by law, {DEVELOPER} is not liable for indirect, incidental or consequential damages arising from your use of the App.</p>
<h2>Changes</h2>
<p>We may update these terms. Continued use of the App after changes means you accept the updated terms.</p>
<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="{DEV_SITE}">{DEV_SITE}</a></p>
</article></main>
"""
write("terms/index.html", page(f"Terms of Use | {GAME}", terms, "terms/", f"Terms of use and subscription terms for {GAME}."))

support = f"""
<main class="wrap"><article class="doc">
<h1>Support</h1>
<p class="meta">We are happy to help with {GAME}.</p>
<div class="contact"><a class="btn" href="mailto:{EMAIL}?subject=Car%20Tow%20Jam%20Support">Email support</a><span>{EMAIL}</span></div>
<p>Please include your device model, iOS version, and the level number if your question is about a level.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How do I play?</summary><p>Tap a car to drive it out. A car can leave only if nothing blocks its path. Cars of the active tow truck's colour load onto the truck; other cars wait in the yellow <strong>P</strong> parking spots. Top cars go to the ferry of their colour. Keep parking spots free so you do not run out of moves.</p></details>
<details><summary>I bought Premium but still see ads</summary><p>Open <strong>Settings &gt; Restore Purchases</strong>. Make sure you are signed in with the same Apple ID that bought the subscription. Optional rewarded videos (like doubling coins) stay available with Premium.</p></details>
<details><summary>How do I cancel Premium?</summary><p>On your iPhone, open <em>Settings &gt; [your name] &gt; Subscriptions</em>, choose Car Tow Jam and tap Cancel. Deleting the App does not cancel the subscription.</p></details>
<details><summary>Can I get a refund?</summary><p>Purchases are handled by Apple. Request a refund at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p></details>
<details><summary>My progress or coins are gone</summary><p>Progress and coins are saved on your device. They are removed if the App is deleted. Premium can always be restored with Restore Purchases.</p></details>
<details><summary>How do I turn off sound, music or vibration?</summary><p>Tap the gear button in the game to open Settings. Use the Music slider and the Sound and Vibration switches.</p></details>
<details><summary>A level feels impossible</summary><p>Every level has a solution. Try parking different blocking cars, and use the parking spots sparingly. You can restart a level from the pause menu.</p></details>
</div>
<h2>Useful links</h2>
<p><a href="../privacy/">Privacy Policy</a> &middot; <a href="../terms/">Terms of Use</a> &middot; <a href="{DEV_SITE}">{DEVELOPER}</a></p>
</article></main>
"""
write("support/index.html", page(f"Support | {GAME}", support, "support/", f"Help and contact for {GAME}."))

target = APP_STORE_URL or ""
download = f"""
<main class="wrap"><article class="doc" style="text-align:center">
<img src="../assets/icon-512.png" alt="" style="width:120px;border-radius:26px;margin-top:8px">
<h1>{GAME}</h1>
<p id="msg">{"Opening the App Store&hellip;" if target else "Coming soon to the App Store. Check back shortly!"}</p>
{f'<p><a class="btn" href="{target}">{APPLE}<span><small>Download on the</small>App Store</span></a></p>' if target else f'<p><a href="{DEV_SITE}">Visit {DEVELOPER}</a></p>'}
</article></main>
{f'<script>location.replace("{target}")</script>' if target else ''}
"""
html = page(f"Download | {GAME}", download, "download/", f"Download {GAME} on the App Store.")
if target: html = html.replace("<head>", f'<head>\n<meta http-equiv="refresh" content="0;url={target}">', 1)
write("download/index.html", html)

write("assets/site.css", CSS.strip() + "\n")
write(".nojekyll", "")
write("app-ads.txt", """# app-ads.txt for Car Tow Jam: Parking Puzzle (Google AdMob)
# AdMob only reads this file from the ROOT of the developer website in the App Store listing:
#   https://kinexapps.com/app-ads.txt
# Replace pub-XXXXXXXXXXXXXXXX with your AdMob publisher ID (AdMob > Settings > Account information),
# remove the leading "# " from the line below, and upload the file to kinexapps.com.
# google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0
""")
write("README.md", f"""# {GAME}: website

Public pages for the App Store listing and AdMob:

| Page | URL |
|---|---|
| Home / Marketing | {BASE} |
| Privacy Policy | {BASE}privacy/ |
| Terms of Use (EULA) | {BASE}terms/ |
| Support | {BASE}support/ |
| QR / download link | {BASE}download/ |

`assets/qr-app-store.png` is the printable QR code (it opens `/download/`, which forwards to the App Store once
`APP_STORE_URL` is set in `build_site.py`). Edit `build_site.py`, run `python3 build_site.py`, then commit and push.
""")
print("site built")
