# Twing-Pulse: Data Warehouse Metadata Analytics

A Snowflake Native App that provides insights into your data warehouse metadata through an interactive Streamlit interface. This is a lightweight version of Twing's comprehensive data warehouse analytics platform.

## 🎯 Purpose

Twing-Pulse analyzes your Snowflake metadata to provide valuable insights about your data warehouse usage, structure, and patterns. This native app serves as an efficient way to:

- Explore metadata from Snowflake system tables
- Visualize key metrics about your data warehouse
- Monitor usage patterns and identify optimization opportunities

## 📁 Project Structure

```plaintext
twing-pulse/
├── app/
│   ├── scripts/
│   │   └── setup_script.sql        # SQL script for initial setup (schemas, roles, grants)
│   ├── src/
│   │   ├── libraries/
│   │   │   ├── __init__.py
│   │   │   └── metadata_analyzer.py # Core metadata analysis logic
│   │   └── streamlit/
│   │       ├── environment.yml     # Python dependencies
│   │       └── streamlit_app.py    # Streamlit UI implementation
│   └── manifest.yml                # Snowflake Native App configuration
├── .gitignore
└── README.md
```

## 🔧 Components

### 1. Metadata Analysis Engine

- Queries Snowflake system tables for metadata
- Analyzes warehouse usage patterns
- Generates insights about data structure and usage

### 2. Streamlit Interface

- Interactive dashboards for metadata visualization
- Real-time query capabilities
- User-friendly filters and controls

## 🚀 Getting Started

1. **Prerequisites**

   - Access to a Snowflake account with appropriate privileges
   - Snowflake role with access to system tables

2. **Installation**

   ```sql
   -- Create application
   CREATE APPLICATION twing_pulse
   FROM manifest='@your_stage/manifest.yml';
   ```

3. **Configuration**
   - Update the connection parameters in `src/streamlit/streamlit_app.py`
   - Modify `app/scripts/setup_script.sql` for your specific requirements

## 🔒 Security

- The app runs with limited permissions defined by the application role
- Only accesses metadata through system tables
- No modification of user data

## 📈 Future Marketplace Release

This app is initially designed to run on internal Snowflake instances but is being developed with the Snowflake Marketplace in mind. Future versions will include:

- Enhanced metadata analysis capabilities
- Additional visualization options
- Extended integration possibilities

## 🤝 Support

For questions or support, please contact:

- Email: support@twing.com
- Documentation: [docs.twing.com](https://docs.twing.com)

---

© 2024 Twing. All rights reserved.
