/* Record a motion pass of the Mira Studio concept site.
   Usage: node _build/record.js   (optional CHROME_PATH env override) */
const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

(async () => {
  let exe = process.env.CHROME_PATH || "";
  if (exe.startsWith("/c/")) exe = "C:" + exe.slice(2);
  exe = exe.trim() || undefined;

  const outDir = path.resolve(__dirname, "shots", "video");
  fs.mkdirSync(outDir, { recursive: true });
  for (const f of fs.readdirSync(outDir)) {
    if (f.endsWith(".webm")) fs.unlinkSync(path.join(outDir, f));
  }

  let browser;
  try {
    browser = await chromium.launch({ headless: true, args: ["--enable-unsafe-swiftshader"] });
  } catch (e) {
    console.log("default launch failed:", e.message.slice(0, 120));
    browser = await chromium.launch({ headless: true, executablePath: exe, args: ["--enable-unsafe-swiftshader"] });
  }

  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    recordVideo: { dir: outDir, size: { width: 1440, height: 900 } },
  });
  const page = await ctx.newPage();
  await page.goto("file:///C:/Users/fortn/concept-sites/mira-studio/index.html");
  await page.waitForTimeout(3800);

  /* slow scroll through the home page */
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  let pos = 0;
  while (pos < H - 900) {
    pos += 34;
    await page.evaluate((p) => window.scrollTo(0, p), pos);
    await page.waitForTimeout(46);
  }
  await page.waitForTimeout(1400);

  /* services page */
  await page.evaluate(() => { location.hash = "#/services"; });
  await page.waitForTimeout(2600);
  await page.evaluate(() => window.scrollBy(0, 320));
  await page.waitForTimeout(1100);

  /* gallery page */
  await page.evaluate(() => { location.hash = "#/gallery"; });
  await page.waitForTimeout(2400);
  await page.evaluate(() => window.scrollBy(0, 640));
  await page.waitForTimeout(1100);

  /* home -> lightbox */
  await page.evaluate(() => { location.hash = "#/"; });
  await page.waitForTimeout(2500);
  await page.evaluate(() => { const g = document.querySelector('[data-gal="g1"]'); if (g) g.click(); });
  await page.waitForTimeout(1900);
  await page.evaluate(() => { const c = document.querySelector("#lightbox [data-close]"); if (c) c.click(); });
  await page.waitForTimeout(900);

  /* contact -> fill + submit -> slip */
  await page.evaluate(() => { location.hash = "#/contact"; });
  await page.waitForTimeout(2400);
  await page.evaluate(() => {
    const set = (id, v) => { const el = document.getElementById(id); if (el) { el.value = v; el.dispatchEvent(new Event("input", { bubbles: true })); } };
    set("fName", "Aarav");
    set("fMail", "aarav@example.com");
    set("fDay", new Date(Date.now() + 3 * 864e5).toISOString().slice(0, 10));
  });
  await page.waitForTimeout(800);
  await page.evaluate(() => { const f = document.getElementById("enqForm"); if (f) f.requestSubmit(); });
  await page.waitForTimeout(1800);
  await page.evaluate(() => { const s = document.querySelector("#enqResult .slip"); if (s) s.scrollIntoView({ block: "center" }); });
  await page.waitForTimeout(1600);

  await page.close();
  await ctx.close();
  await browser.close();

  const webms = fs.readdirSync(outDir).filter((f) => f.endsWith(".webm"));
  console.log("video done:", webms.join(", "));
})().catch((e) => {
  console.error("REC FAIL", e.message.slice(0, 300));
  process.exit(1);
});
