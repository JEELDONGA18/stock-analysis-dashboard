# LeetCode Data Fetcher 🧠📊

This Python script allows you to fetch detailed LeetCode user statistics using GraphQL. It collects and organizes valuable insights such as profile information, solved problems, contest history, badges, and language usage—all in one place.

---

## 🚀 Features

✅ **User Profile Details**
- Username, Real Name, Bio, Country, Global Ranking, and Reputation

✅ **Solved Problems Statistics**
- Total problems by difficulty (Easy/Medium/Hard)
- Accepted submissions by difficulty

✅ **Topic-wise Problem Solving Stats**
- Solved problems categorized by:
  - Fundamental
  - Intermediate
  - Advanced

✅ **Contest Participation History**
- Total contests participated
- Current rating
- Global ranking
- Top percentage
- Full contest history (title, time, score, rank, etc.)

✅ **Badges Earned**
- List of earned badges with:
  - Name, Display Name, Short Name, Creation Date, ID

✅ **Language-wise Problem Stats**
- Problems solved per programming language

🔄 **Central Data Aggregator**
- `fetch_all_leetcode_data(username)` function (assumed)
- Aggregates all of the above into one structured dataset (likely JSON)

---

## 🛠️ Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
