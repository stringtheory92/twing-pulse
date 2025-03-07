-- Create application role
CREATE OR REPLACE APPLICATION ROLE your_app_role;

-- Create schema for the application
CREATE OR REPLACE SCHEMA your_app_schema;

-- Grant usage on schema to application role
GRANT USAGE ON SCHEMA your_app_schema TO APPLICATION ROLE your_app_role;

-- Create Streamlit app within the schema
CREATE OR REPLACE STREAMLIT your_app_schema.streamlit_app
  FROM 'src/streamlit'
  MAIN_FILE = 'streamlit_app.py';

-- Grant usage on Streamlit app to application role
GRANT USAGE ON STREAMLIT your_app_schema.streamlit_app TO APPLICATION ROLE your_app_role;
