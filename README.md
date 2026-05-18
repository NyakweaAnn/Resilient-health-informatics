# Emergency Syndromic Surveillance Data Collection Framework

## 🌍 Context & Operational Overview
In an acute humanitarian crisis or disease outbreak, frontline health infrastructure often operates with zero internet connectivity and limited power. This repository contains a production-ready data collection framework built on the global open-source **XLSForm standard** (the engine driving **WHO EWARS in a box**, **KoboToolbox**, and **ODK**).

The architecture of this form is engineered with an **"Offline-First" philosophy**. Rather than relying on cloud servers to clean data post-submission, all validation logic and data constraints run locally on the mobile device's edge processor. This prevents corrupt data entry at the clinic level, reduces transmission payload sizes, and guarantees relational integrity when field data is merged for epidemiological analysis.

## 🛠️ Core Engineering Features Built-In
* **Edge-Level Constraints:** Implements deterministic boundary parameters on physiological metrics (e.g., axillary temperature checks between `34.0°C` and `42.0°C`) to eliminate typographical entry errors before the database write-action occurs.
* **Contextual Conditional Visibility (Skip Logic):** Utilizes relational evaluation rules (`${patient_gender} = 'female'`) to dynamically display or encapsulate specific clinical fields, heavily reducing survey fatigue for high-stress frontline responders.
* **Metadata Uniformity:** Restricts data collection points to explicit key-value dropdown pairings (`choices` sheet architecture), systematically eliminating free-text fields to ensure clean downstream analytical joins.
* **Automated Outbreak Detection Engine (outbreak_alert_system.py): Implements a rolling-window statistical surveillance algorithm ($\mu + 2\sigma$) using pandas and numpy to programmatically flag syndromic case spikes, eliminating the lag between field entry and epidemiological response.

## 🚀 How to Preview
1. Download the `emergency_surveillance_template.xlsx` file from this repository.
2. Upload the file to the open-source validator at [getodk.org/xlsform](https://getodk.org/xlsform/).
3. Click **Preview in browser** to interact with the mobile UI, dynamic skip logic, and localized data constraints.
