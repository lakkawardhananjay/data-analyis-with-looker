# Cricket Stats Project

This project aims to analyze cricket statistics using Google Cloud services and visualize the insights using Looker. The project leverages various GCP services including Cloud Storage, Cloud Functions, Cloud Composer, Dataflow, and BigQuery for data processing, storage, and analysis.

## Overview

Cricket is a popular sport with a vast amount of data generated from matches, players, teams, and tournaments. This project utilizes Google Cloud services to ingest, process, and analyze cricket statistics, providing valuable insights into player performance, team dynamics, and match outcomes.
## Services used in architecture
![Cric Buzz API](https://github.com/lakkawardhananjay/data-analyis-with-looker/assets/92675267/c0b9d261-3d58-488e-acb1-4522b1010f4d)

## GCP Services Used

### 1. Cloud Storage

- **Purpose:** Store raw and processed data files.
- **Usage:** Raw cricket data files are uploaded to Cloud Storage buckets for ingestion into the pipeline. Processed data is also stored for archival and further analysis.

### 2. Cloud Functions

- **Purpose:** Trigger data processing workflows.
- **Usage:** Cloud Functions are used to automatically trigger Dataflow jobs upon the arrival of new data files in Cloud Storage. This ensures seamless data processing and analysis.

### 3. Cloud Composer

- **Purpose:** Orchestrate data pipelines.
- **Usage:** Cloud Composer is utilized to create and manage workflows for data processing. DAGs (Directed Acyclic Graphs) are defined to orchestrate the sequence of tasks involved in ingesting, processing, and loading data into BigQuery.

### 4. Dataflow

- **Purpose:** Process and transform large volumes of data.
- **Usage:** Dataflow pipelines are employed for real-time and batch processing of cricket statistics. Data is transformed, cleaned, and enriched before being loaded into BigQuery for analysis.

### 5. BigQuery

- **Purpose:** Analyze and query structured data.
- **Usage:** BigQuery serves as the data warehouse for storing and analyzing cricket statistics. SQL queries are executed to extract insights, generate reports, and create visualizations.

## Usage

1. **Data Ingestion:** Upload raw cricket data files to designated Cloud Storage buckets.
2. **Data Processing:** Cloud Functions trigger Dataflow jobs for processing and transforming the data.
3. **Workflow Orchestration:** Define and manage data pipelines using Cloud Composer DAGs.
4. **Analysis and Visualization:** Use Looker to connect to BigQuery and create dashboards and reports for analyzing cricket statistics.

## Contributing

Contributions to this project are welcome! Feel free to submit issues, feature requests, or pull requests on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
