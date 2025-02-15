# app.py
import streamlit as st
from crew import Deepeek  # Adjust import if needed (e.g., from deepeek.crew import Deepeek)

def main():
    st.title("Deepeek CrewAI App")

    # Let the user provide a topic or query
    topic = st.text_input("Enter your topic/question", value="Does Benin have a centralized entry/exit system...?")

    # When the user clicks the "Run Tasks" button, we'll run your entire Crew pipeline
    if st.button("Run Tasks"):
        st.write("Running tasks. Please wait...")

        # Pass the user’s topic to your Crew as inputs
        inputs = {"topic": topic}

        try:
            # 1) Create an instance of the Deepeek crew
            dp = Deepeek().crew()

            # 2) Kick off the tasks with the user-provided inputs
            dp.kickoff(inputs=inputs)

            st.success("Crew tasks completed successfully!")

            # 3) Optionally, read the 'report.md' file if your reporting_task writes there
            try:
                with open("report.md", "r", encoding="utf-8") as f:
                    report_content = f.read()
                st.markdown("### Final Report")
                st.markdown(report_content)
            except FileNotFoundError:
                st.warning("No 'report.md' file found. Make sure reporting_task produces it.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
