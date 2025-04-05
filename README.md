# 🧠 LeetCode User Analytics Dashboard

A powerful and developer-friendly Python module to fetch and visualize **comprehensive LeetCode user statistics**.  
Gain insights into problem-solving behavior, contest participation, badge achievements, topic proficiency, and much more.

---

## 🚀 Features

### 🧑‍💻 User Profile Details
- Username & Real Name  
- Bio (About Me)  
- Country  
- Global Ranking  
- Reputation

### 📊 Solved Problem Statistics
- Total number of questions per difficulty (Easy, Medium, Hard)  
- Number of accepted submissions per difficulty

### 🧠 Topic-wise Problem Solving Stats
- Problems solved categorized by:
  - Fundamental
  - Intermediate
  - Advanced

### 🏁 Contest Participation History
- Total contests participated
- Current rating
- Global ranking and top percentage
- Full contest history with:
  - Contest title
  - Start time
  - Rank
  - Score
  - Problems solved
  - Total problems

### 🏅 Badges Earned
- List of earned badges with:
  - Badge name
  - Display name
  - Creation date
  - Short name
  - ID

### 💻 Language-wise Problem Stats
- Problems solved per programming language used

### 🔄 Central Aggregation
- `fetch_all_leetcode_data(username)` collects all of the above in a single call and returns a complete dataset (as JSON)

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/leetcode-analytics.git
cd leetcode-analytics
pip install -r requirements.txt
