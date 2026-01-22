# Hyperliquid Vault Research – Quantitative & Risk Evaluation

This repository contains a full quantitative and fundamental research pipeline for evaluating the Hyperliquid protocol for potential inclusion in Token Metrics vault strategies. The project mirrors a real institutional investment research workflow, combining protocol due diligence, quantitative yield analysis, structured risk scoring, correlation assessment, and the production of a defensible, actionable investment recommendation.

The objective is to produce a reproducible, data-driven framework that supports professional-grade decision-making in a live portfolio context.

## Research Objectives

The project aims to:
- Conduct fundamental protocol due diligence, including governance, administrative risk, and revenue sustainability.
- Build a quantitative framework for analyzing protocol efficiency, yield behavior, and regime sensitivity.
- Develop a structured risk scoring model combining quantitative and qualitative factors.
- Assess correlation and concentration risks relative to broader crypto market dynamics.
- Produce a clear, actionable investment recommendation including allocation sizing and monitoring triggers.

## Methodology

The research framework integrates:
- On-chain and protocol-level data collection.
- Time-series analysis of protocol activity and economic outputs.
- Quantitative efficiency metrics, including fee-to-TVL ratios and volatility-adjusted measures.
- Regime-based risk classification.
- Scenario-based stress interpretation.
- Structured qualitative assessment of governance, upgrade risk, and operational controls.

All analytical logic is implemented in modular Python scripts to ensure reproducibility and auditability.

## Project Structure

project/
├── README.md  
├── data/  
│   ├── raw/           # Raw downloaded datasets  
│   └── processed/     # Cleaned and analysis-ready datasets  
├── src/  
│   ├── fetch/         # Data ingestion modules  
│   ├── metrics/       # Quantitative metric computation  
│   ├── risk/          # Risk scoring and regime classification  
│   ├── portfolio/     # Correlation and portfolio impact analysis  
│   └── run.py         # Main pipeline execution script  
├── outputs/  
│   ├── charts/        # Generated figures  
│   └── tables/        # Summary tables and metrics  

## Data Sources

Primary data sources include:
- DeFiLlama API for TVL and protocol-level fee metrics.
- Protocol-native endpoints for operational indicators.
- Public on-chain data proxies for utilization, trading volume, and volatility dynamics.

All data is collected at daily frequency and cached locally to ensure reproducibility.

## Analytical Pipeline

The research pipeline follows the steps below:
1. Data ingestion from public APIs and protocol endpoints.
2. Data cleaning, normalization, and frequency alignment.
3. Quantitative metric computation.
4. Qualitative protocol risk assessment.
5. Structured risk scoring.
6. Correlation and concentration risk analysis.
7. Generation of charts and summary tables.

## How To Run

Install dependencies:

pip install -r requirements.txt

Run the pipeline:

python src/run.py

This executes the full research workflow and generates outputs inside the outputs directory.

## Outputs

All generated figures and tables are saved inside:

outputs/

Including:
- Quantitative metric tables
- Time-series visualizations
- Risk assessment summaries
- Charts used in the investment memo

## Reproducibility Notes

All analytical logic is fully scripted and deterministic given identical data snapshots. No manual spreadsheet operations are required. This ensures full reproducibility and independent auditability.
