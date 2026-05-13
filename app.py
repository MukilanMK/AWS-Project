from flask import Flask, render_template_string

app = Flask(__name__)


PAGE_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dr APJ Abdul Kalam | Interactive Profile</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #f5f7fa;
      --card: #ffffff;
      --ink: #14253d;
      --muted: #4b5f78;
      --brand: #0b5ed7;
      --brand-soft: #dbe8ff;
      --accent: #1f9d8b;
      --ring: rgba(11, 94, 215, 0.25);
      --shadow: 0 18px 40px rgba(20, 37, 61, 0.12);
      --radius: 18px;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(900px 500px at 100% -20%, #d9ecff 0%, rgba(217, 236, 255, 0) 65%),
        radial-gradient(700px 400px at -20% 10%, #e6fff5 0%, rgba(230, 255, 245, 0) 60%),
        var(--bg);
      font-family: "Space Grotesk", sans-serif;
      line-height: 1.6;
    }

    .wrap {
      width: min(1100px, 92%);
      margin: 0 auto;
      padding: 28px 0 50px;
    }

    .hero {
      background: linear-gradient(135deg, #ffffff 0%, #f2f7ff 100%);
      border: 1px solid #dce7f7;
      border-radius: calc(var(--radius) + 6px);
      padding: 28px;
      box-shadow: var(--shadow);
      overflow: hidden;
      position: relative;
      animation: rise 0.6s ease;
    }

    .hero::after {
      content: "";
      position: absolute;
      right: -60px;
      top: -80px;
      width: 260px;
      height: 260px;
      border-radius: 50%;
      background: linear-gradient(145deg, #d7e9ff, #e6fff7);
      opacity: 0.8;
      z-index: 0;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 20px;
      position: relative;
      z-index: 1;
    }

    h1 {
      margin: 0;
      font-size: clamp(1.9rem, 3vw, 3rem);
      letter-spacing: -0.02em;
    }

    .subtitle {
      color: var(--muted);
      margin-top: 8px;
      font-size: 1.05rem;
    }

    .lifespan {
      display: inline-block;
      margin-top: 14px;
      padding: 7px 12px;
      border-radius: 999px;
      background: var(--brand-soft);
      color: #12428f;
      font-weight: 700;
      font-size: 0.88rem;
    }

    .quote-box {
      background: #0f2f59;
      color: #eaf1fb;
      border-radius: var(--radius);
      padding: 18px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      min-height: 180px;
    }

    .quote {
      font-family: "Source Serif 4", serif;
      font-size: 1.15rem;
      margin: 0 0 8px;
    }

    .quote-meta {
      color: #c0d4ef;
      font-size: 0.88rem;
      margin: 0;
    }

    .grid {
      margin-top: 22px;
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 16px;
    }

    .card {
      background: var(--card);
      border: 1px solid #dde6f3;
      border-radius: var(--radius);
      padding: 18px;
      box-shadow: 0 8px 18px rgba(20, 37, 61, 0.06);
      animation: rise 0.6s ease;
    }

    .card h2 {
      margin: 0 0 10px;
      font-size: 1.1rem;
    }

    .summary { grid-column: span 7; }
    .highlights { grid-column: span 5; }
    .timeline { grid-column: span 8; }
    .facts { grid-column: span 4; }
    .books { grid-column: span 12; }

    ul.clean {
      margin: 0;
      padding-left: 18px;
    }

    .timeline-controls {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 12px;
    }

    .chip {
      border: 1px solid #cbd8ea;
      background: #f8fbff;
      color: #24476f;
      border-radius: 999px;
      padding: 6px 11px;
      cursor: pointer;
      font-size: 0.85rem;
      transition: transform 0.15s ease, border-color 0.15s ease;
    }

    .chip:hover { transform: translateY(-1px); }
    .chip.active { background: var(--brand); color: #fff; border-color: var(--brand); }

    .timeline-item {
      border-left: 3px solid #c7d8f2;
      padding-left: 12px;
      margin: 0 0 12px;
    }

    .timeline-item strong { color: #133f78; }
    .timeline-item small { color: var(--muted); display: block; }

    .stat-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
    }

    .stat {
      background: #f5faff;
      border: 1px solid #d7e5f8;
      border-radius: 14px;
      padding: 12px;
    }

    .stat .num {
      font-weight: 700;
      color: #083b84;
      font-size: 1.2rem;
    }

    .book-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
    }

    .book {
      border: 1px solid #d8e3f2;
      border-radius: 14px;
      padding: 12px;
      background: linear-gradient(180deg, #ffffff 0%, #f7faff 100%);
    }

    footer {
      margin-top: 22px;
      color: var(--muted);
      font-size: 0.88rem;
      text-align: center;
    }

    @keyframes rise {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 900px) {
      .hero-grid { grid-template-columns: 1fr; }
      .summary, .highlights, .timeline, .facts, .books { grid-column: span 12; }
    }
  </style>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <div class="hero-grid">
        <div>
          <h1>{{ profile.name }}</h1>
          <p class="subtitle">{{ profile.title }}</p>
          <span class="lifespan">{{ profile.lifespan }}</span>
        </div>
        <aside class="quote-box">
          <p class="quote" id="quoteText"></p>
          <p class="quote-meta">Dr APJ Abdul Kalam</p>
        </aside>
      </div>
    </section>

    <section class="grid">
      <article class="card summary">
        <h2>Who He Was</h2>
        <p>{{ profile.summary }}</p>
      </article>

      <article class="card highlights">
        <h2>Major Highlights</h2>
        <ul class="clean">
          {% for item in profile.highlights %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </article>

      <article class="card timeline">
        <h2>Life Timeline</h2>
        <div class="timeline-controls" id="timelineControls">
          <button class="chip active" data-filter="all">All</button>
          <button class="chip" data-filter="education">Education</button>
          <button class="chip" data-filter="science">Science</button>
          <button class="chip" data-filter="leadership">Leadership</button>
          <button class="chip" data-filter="legacy">Legacy</button>
        </div>
        <div id="timelineList">
          {% for item in timeline %}
          <div class="timeline-item" data-kind="{{ item.kind }}">
            <strong>{{ item.year }}</strong>
            <small>{{ item.detail }}</small>
          </div>
          {% endfor %}
        </div>
      </article>

      <aside class="card facts">
        <h2>Quick Facts</h2>
        <div class="stat-grid">
          <div class="stat"><div class="num">11th</div><div>President of India</div></div>
          <div class="stat"><div class="num">2002-2007</div><div>Presidential Term</div></div>
          <div class="stat"><div class="num">Bharat Ratna</div><div>Highest Civilian Honor</div></div>
          <div class="stat"><div class="num">People's President</div><div>Public Recognition</div></div>
        </div>
      </aside>

      <article class="card books">
        <h2>Notable Books</h2>
        <div class="book-list">
          {% for book in books %}
          <div class="book">
            <strong>{{ book.title }}</strong>
            <div>{{ book.note }}</div>
          </div>
          {% endfor %}
        </div>
      </article>
    </section>

    <footer>
      Single-page educational profile built with Flask.
    </footer>
  </main>

  <script>
    const quotes = [
      "Dream is not that which you see while sleeping; it is something that does not let you sleep.",
      "If you want to shine like a sun, first burn like a sun.",
      "Excellence is a continuous process and not an accident."
    ];

    let q = 0;
    const quoteText = document.getElementById("quoteText");
    function rotateQuote() {
      quoteText.textContent = quotes[q % quotes.length];
      q += 1;
    }
    rotateQuote();
    setInterval(rotateQuote, 4500);

    const chips = Array.from(document.querySelectorAll(".chip"));
    const items = Array.from(document.querySelectorAll(".timeline-item"));
    chips.forEach((chip) => {
      chip.addEventListener("click", () => {
        chips.forEach((c) => c.classList.remove("active"));
        chip.classList.add("active");
        const selected = chip.dataset.filter;
        items.forEach((item) => {
          item.style.display = selected === "all" || item.dataset.kind === selected ? "block" : "none";
        });
      });
    });
  </script>
</body>
</html>
"""


@app.get("/")
def home():
    profile = {
        "name": "Dr APJ Abdul Kalam",
        "title": "Scientist, Teacher, and Former President of India",
        "lifespan": "1931-2015",
        "summary": (
            "Avul Pakir Jainulabdeen Abdul Kalam was an Indian aerospace scientist and "
            "statesman. He made major contributions to India's civilian space and defense "
            "programs, served as the 11th President of India, and became a national symbol "
            "of humility, discipline, and youth inspiration."
        ),
        "highlights": [
            "Born in Rameswaram, Tamil Nadu, into a modest family and educated through determination.",
            "Studied Physics at St. Joseph's College and Aerospace Engineering at MIT, Chennai.",
            "Worked at DRDO and later ISRO, including leadership in launch vehicle programs.",
            "Played major roles in strategic missile development programs, earning the title 'Missile Man of India'.",
            "Served as the President of India and remained deeply connected to students and teachers.",
            "Received the Bharat Ratna and wrote books focused on vision, innovation, and nation-building.",
        ],
    }

    timeline = [
        {"year": "1931", "detail": "Born in Rameswaram, Tamil Nadu.", "kind": "legacy"},
        {"year": "1950s", "detail": "Completed studies in Physics and Aerospace Engineering.", "kind": "education"},
        {"year": "1960", "detail": "Joined DRDO as a scientist.", "kind": "science"},
        {"year": "1969", "detail": "Joined ISRO and contributed to satellite launch vehicle efforts.", "kind": "science"},
        {"year": "1980s", "detail": "Led key efforts in India's guided missile development programs.", "kind": "science"},
        {"year": "1990s", "detail": "Served in senior scientific advisory and defense technology roles.", "kind": "leadership"},
        {"year": "2002-2007", "detail": "Served as the 11th President of India.", "kind": "leadership"},
        {"year": "Post-2007", "detail": "Focused on teaching, youth engagement, and innovation missions.", "kind": "legacy"},
        {"year": "2015", "detail": "Passed away while delivering a lecture to students in Shillong.", "kind": "legacy"},
    ]

    books = [
        {"title": "Wings of Fire", "note": "Autobiographical journey from childhood to scientific leadership."},
        {"title": "Ignited Minds", "note": "A call for youth-driven national transformation."},
        {"title": "India 2020", "note": "Vision document for transforming India into a developed nation."},
        {"title": "My Journey", "note": "Personal stories, values, and life lessons."},
    ]

    return render_template_string(PAGE_HTML, profile=profile, timeline=timeline, books=books)


if __name__ == "__main__":
    app.run(debug=True)
