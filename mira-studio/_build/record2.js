/* Lean motion recorder v2 — bounded by watchdog, stderr logging. */
const path = require("path"), fs = require("fs");
const { chromium } = require("playwright");
const log = (m) => process.stderr.write("[rec] " + m + "\n");
setTimeout(() => { log("WATCHDOG abort"); process.exit(2); }, 150000);

(async () => {
  const outDir = path.resolve(__dirname, "shots", "video");
  fs.mkdirSync(outDir, { recursive: true });
  for (const f of fs.readdirSync(outDir)) if (f.endsWith(".webm")) fs.unlinkSync(path.join(outDir, f));

  const exe = "C:/Users/fortn/AppData/Local/ms-playwright/chromium-1243/chrome-win64/chrome.exe";
  log("launching");
  const browser = await chromium.launch({
    headless: true,
    executablePath: fs.existsSync(exe) ? exe : undefined,
    args: ["--enable-unsafe-swiftshader", "--disable-gpu"],
  });
  log("launched");

  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    recordVideo: { dir: outDir, size: { width: 1280, height: 800 } },
  });
  const page = await ctx.newPage();
  page.setDefaultTimeout(20000);

  log("goto");
  await page.goto("file:///C:/Users/fortn/concept-sites/mira-studio/index.html", { waitUntil: "load", timeout: 30000 });
  log("loaded");
  await page.waitForTimeout(3600);

  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  log("H=" + H);
  let pos = 0;
  while (pos < H - 880) {
    pos += 56;
    await page.evaluate((p) => window.scrollTo(0, p), pos);
    await page.waitForTimeout(38);
  }
  log("home scrolled");
  await page.waitForTimeout(900);

  await page.evaluate(() => { location.hash = "#/services"; });
  await page.waitForTimeout(2400);
  await page.evaluate(() => window.scrollBy(0, 360));
  await page.waitForTimeout(1000);
  log("services done");

  await page.evaluate(() => { location.hash = "#/contact"; });
  await page.waitForTimeout(2400);
  await page.evaluate(() => {
    const set = (id, v) => { const el = document.getElementById(id); if (el) { el.value = v; el.dispatchEvent(new Event("input", { bubbles: true })); } };
    set("fName", "Aarav");
    set("fMail", "aarav@example.com");
    set("fDay", new Date(Date.now() + 3 * 864e5).toISOString().slice(0, 10));
    const f = document.getElementById("enqForm");
    if (f) f.requestSubmit();
  });
  await page.waitForTimeout(1600);
  await page.evaluate(() => { const s = document.querySelector("#enqResult .slip"); if (s) s.scrollIntoView({ block: "center" }); });
  await page.waitForTimeout(1500);

  log("closing");
  await page.close();
  await ctx.close();
  await browser.close();
  log("done");
  const webms = fs.readdirSync(outDir).filter((f) => f.endsWith(".webm"));
  log("webm: " + webms.join(", "));
  process.exit(0);
})().catch((e) => {
  log("FAIL " + String(e).slice(0, 200));
  process.exit(1);
});
