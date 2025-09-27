## 🌍 Trip Planner Agent

Plan your dream trip to any city worldwide with real-time data ✈️🌆.
This intelligent agent helps you make informed travel decisions by combining live information, smart planning, and cost estimates—all in one place.

---

## 🚀 Features

- ✅ Real-Time Weather Info – Get up-to-date forecasts for your destination.
- ✅ Attractions & Activities – Discover must-see spots and fun things to do.
- ✅ Hotel Cost Estimation – Check average accommodation prices.
- ✅ Currency Conversion – Convert your budget into local currency instantly.
- ✅ Itinerary Planning – Create a personalized day-by-day schedule.
- ✅ Total Expense Calculation – Estimate your overall trip cost.
- ✅ Smart Summary Generation – Receive a clear, shareable summary of your trip.

---

## 🛠️ Tech Stack

- Programming Language: Python 🐍(uv package)

- APIs & Integrations: Weather API, Currency Exchange API, Tavily API

- Frameworks/Libraries: LangGraph, Requests(FastAPI), Streamlit

---

## Installation
To set up the Trip Planner Agent locally, follow these steps:

1. Clone the repository to your local machine:
```python
   git clone https://github.com/samanta-sc/Trip-Planner-Agent.git
```
2. Navigate to the project directory:
```python
   cd Trip-Planner-Agent
```
3. Install the required Python packages using uv:
```python
uv pip install -r requirements.txt
```
4. Set up environment variables:
  - Define the necessary environment variables such as database connection strings, API keys, etc.
5. Expose the API
```
uvicorn main:app
```
6. Run the Streamlit application:
```
streamlit run app.py
```

---

## 📸 Demo

<table>
  <tr>
    <td>Trip Planner Agent Day-wise Plan</td>
     <td>Trip Planner Agent Cost, Weather</td>
  </tr>
  <tr>
    <td><img align="left" src="resources/Screenshot (24).png" width=350 height=480></td>
    <td><img align="left" src="resources/Screenshot (25).png" width=350 height=480></td>
  </tr>
 </table>

 ---

## 🎯 Use Cases
- 🧳 Travelers looking for a quick, budget-friendly plan.

- 🌎 Travel agencies exploring AI-powered assistants.

- 💡 Showcasing integration of real-time APIs + AI planning.
