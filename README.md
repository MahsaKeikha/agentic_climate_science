# F85 Agentic Climate Science

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for climate-science research across problem formulation, data and provenance review, climate modeling, scenario analysis, uncertainty and attribution reasoning, reproducibility, and qualified human scientific review.

F85 is intended as a reusable research framework for climate evidence synthesis and model-based analysis. It keeps observations, reconstructions, model output, scenarios, assumptions, uncertainty, attribution claims, and policy judgments explicitly separated so that the strength of a conclusion remains proportional to the evidence supporting it.

This repository supports scientific research and reporting. It does not fabricate observations, claim certainty beyond the evidence, make binding policy decisions, replace domain experts, or exercise autonomous scientific or governmental authority.

## Research lifecycle

```text
climate question
      |
      v
problem formulation
      |
      v
data + provenance review
      |
      v
climate modeling + scenarios
      |
      v
uncertainty + attribution
      |
      v
qualified human review
```

The workflow is fail closed. Missing provenance, incompatible datasets, invalid assumptions, scenario mismatch, unresolved uncertainty, unsupported attribution, causal overclaiming, contradictory evidence, or reproducibility gaps remain visible as blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Problem Agent | Defines the climate question, variables, geography, time horizon and claim type | What is being estimated or explained, over what region and period, and at what scale? |
| Data Agent | Reviews observations, reconstructions, model data, provenance and preprocessing | Are the data appropriate, traceable, comparable and sufficiently characterized? |
| Modeling Agent | Reviews model selection, assumptions, scenarios, ensembles and comparison logic | What model evidence is relevant and what can it legitimately support? |
| Uncertainty Agent | Reviews uncertainty, sensitivity, attribution strength and competing explanations | How confident is the conclusion, and which uncertainties materially affect it? |
| Reviewer Agent | Represents qualified scientific synthesis and release authority | Has an appropriately qualified human reviewed the evidence, assumptions and limitations? |

No specialist agent independently declares certainty, settles a contested attribution question, or issues policy mandates.

## Repository structure

```text
AGENTS/
├── problem_agent.py
├── data_agent.py
├── modeling_agent.py
├── uncertainty_agent.py
└── reviewer_agent.py

SKILLS/
├── problem_decomposition.py
├── evidence_discipline.py
├── provenance_tracking.py
├── uncertainty_reasoning.py
└── human_review.py

TOOLS/
├── assumption_tracker.py
├── data_validator.py
├── evidence_register.py
├── result_formatter.py
└── review_gate.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates scientific reasoning from deterministic evidence handling, workflow state, safety controls, evaluation and observability.

## Problem formulation

Climate questions should specify the claim before datasets or models are selected.

A useful research record can include:

```text
question_id
variable
claim_type
region
spatial_scale
time_period
baseline_period
season_or_month
observational_source
model_source
scenario
forcing_assumptions
comparison_method
uncertainty_method
provenance
```

Claim types can include description, trend estimation, projection, detection, attribution, mechanism analysis, risk characterization, scenario comparison, or impact assessment. These are not interchangeable.

## Weather, climate and climate variability

F85 distinguishes short-term weather from climate statistics and long-term climate change.

A single storm, heatwave, cold spell, flood, drought, wildfire season, or unusual year should not by itself be treated as proof for or against a long-term climate trend.

Likewise, long-term trends do not mean every local event has the same cause.

The temporal and spatial scale of the evidence should match the claim.

## Observational data

Climate observations can originate from:

- surface stations
- ocean observations
- radiosondes
- satellites
- reanalysis products
- weather radar
- buoys
- ice cores
- tree rings
- corals
- sediment records
- glacier observations
- sea-level records
- atmospheric composition measurements

Each source has different coverage, uncertainty, calibration history and processing assumptions.

`TOOLS/data_validator.py` supports deterministic validation of structured data records.

## Data provenance

A defensible analysis should preserve enough information to trace every important result to its source.

Relevant provenance can include:

```text
dataset_name
provider
version
variable
units
spatial_resolution
temporal_resolution
coverage
retrieval_or_measurement_method
quality_control
bias_correction
regridding
masking
missing_data_method
baseline
processing_code
access_date
```

Derived products should retain lineage to their underlying observations or model runs.

## Homogenization and measurement changes

Long climate records can contain non-climatic changes caused by station moves, instrument changes, observation practices, satellite transitions, urban development, coverage changes or processing updates.

Research review should identify whether relevant datasets have been homogenized or adjusted and why.

An adjustment is not automatically evidence of manipulation. It is a methodological choice that should be documented, justified and open to sensitivity analysis.

## Missing data and coverage

Climate datasets can have uneven spatial and temporal coverage.

Review should consider:

- missing observations
- changing station density
- ocean coverage
- polar coverage
- satellite-era transitions
- interpolation
- infilling
- gridding
- spatial weighting

The uncertainty created by incomplete coverage should be reflected in the conclusion.

## Reanalysis data

Reanalysis combines observations with numerical weather-prediction models through data assimilation.

F85 treats reanalysis as a model-observation synthesis, not as raw direct observation.

When using reanalysis, record the product version, assimilation system, resolution, relevant input observations, and known limitations for the variable being studied.

## Climate models

Climate models represent interacting components of the Earth system, including atmosphere, ocean, land, cryosphere and, in many models, biogeochemical processes.

Model review can include:

- model family
- model version
- resolution
- forcing configuration
- parameterizations
- initialization
- ensemble member
- historical experiment
- scenario experiment
- boundary conditions
- coupling
- known biases

A model result should not be interpreted independently of its experiment configuration.

## Model hierarchy

Different scientific questions require different levels of model complexity.

Potential model classes include:

- conceptual energy-balance models
- statistical models
- regional climate models
- global climate models
- Earth system models
- process models
- impact models
- emulators and surrogate models
- machine-learning models

F85 is method-neutral. Model complexity should be appropriate to the question rather than treated as evidence quality by itself.

## Model evaluation

Model evaluation asks whether a model represents relevant observed climate behavior well enough for the intended analysis.

Evaluation can consider:

- climatology
- seasonal cycle
- trends
- variability
- teleconnections
- circulation patterns
- extremes
- energy balance
- precipitation
- temperature
- ocean behavior
- cryosphere behavior

Performance for one variable or region does not guarantee performance for another.

## Ensembles

Climate research frequently uses ensembles to characterize internal variability, model differences and scenario uncertainty.

Relevant ensemble types include:

- initial-condition ensembles
- multi-model ensembles
- perturbed-physics ensembles
- scenario ensembles

Ensemble members should not automatically be treated as statistically independent samples. Models can share code, parameterizations, institutional lineage or common structural assumptions.

## Scenario analysis

A scenario is a conditional representation of a possible future, not a prediction that the scenario will necessarily occur.

Scenario records should identify:

```text
scenario_name
scenario_family
forcing_pathway
emissions_or_concentration_assumptions
socioeconomic_assumptions
land_use_assumptions
time_horizon
baseline
```

Results from different scenarios should not be mixed without explaining the differences in their assumptions.

## Projection versus prediction

F85 distinguishes projections from predictions.

A climate projection is commonly conditional on specified forcing or socioeconomic assumptions. A near-term initialized climate prediction may have a different scientific structure.

The final report should use terminology that matches the actual experiment.

## Baselines and anomalies

Temperature and other climate anomalies depend on a defined reference period.

Every anomaly-based result should preserve:

- baseline period
- spatial aggregation
- temporal aggregation
- dataset
- units

Comparisons using different baselines require explicit conversion or qualification.

## Trend analysis

Trend claims should specify:

- start and end dates
- variable
- spatial domain
- season
- statistical model
- treatment of autocorrelation
- uncertainty interval
- sensitivity to endpoints where relevant

Short-window trends can be strongly affected by internal variability. The selected period should be scientifically justified.

## Internal variability

Climate varies naturally across many time scales.

Relevant modes and processes can include ocean-atmosphere variability, volcanic forcing, solar variability and other internal or external influences.

Internal variability can temporarily amplify or offset a forced trend at regional or shorter time scales. It should be considered when interpreting observations and model comparisons.

## Detection and attribution

Detection and attribution are stronger scientific claims than trend description.

**Detection** asks whether an observed change is distinguishable from expected internal variability.

**Attribution** evaluates the relative contributions of different causal factors to an observed change.

Attribution analysis can involve:

- greenhouse-gas forcing
- aerosols
- land-use change
- solar forcing
- volcanic forcing
- internal variability
- combinations of forcings

F85 must not convert correlation or model agreement into certain causal attribution without appropriate evidence.

## Event attribution

Extreme-event attribution asks how climate conditions or forcings may have changed the probability or intensity of a class of event.

A responsible event-attribution result should identify:

- event definition
- geographic domain
- observational evidence
- model ensembles
- counterfactual construction
- probability or intensity metric
- uncertainty
- model adequacy
- sensitivity to event definition

The system should avoid simplistic statements that climate change was the sole cause of an individual event unless the evidence specifically supports such wording.

## Uncertainty

Climate uncertainty has multiple sources.

The Uncertainty Agent can distinguish:

- observational uncertainty
- measurement uncertainty
- sampling uncertainty
- internal variability
- model structural uncertainty
- parameter uncertainty
- scenario uncertainty
- downscaling uncertainty
- impact-model uncertainty
- statistical uncertainty

These sources matter differently depending on region, variable and time horizon.

## Uncertainty communication

Uncertainty is not the same as ignorance and should not be hidden or exaggerated.

A useful report separates:

```text
what_is_observed
what_is_modeled
what_is_inferred
confidence
uncertainty_sources
sensitivity
limitations
```

Where probability language is used, the meaning and basis should be clear.

## Sensitivity analysis

Sensitivity analysis can test whether a conclusion depends strongly on methodological choices.

Examples include:

- alternate datasets
- alternate baselines
- alternate trend windows
- alternate spatial masks
- alternate model subsets
- alternate weighting methods
- alternate statistical specifications
- alternate scenarios
- alternate downscaling methods

A conclusion that disappears under reasonable alternatives should be reported as sensitive rather than robust.

## Model weighting

Multi-model analyses sometimes weight models according to performance, independence or other criteria.

Weighting choices should be documented because they can materially change ensemble results.

F85 should not silently treat every model as either equally informative or fully independent without examining the scientific rationale.

## Downscaling

Global model output is often downscaled for regional analysis.

Methods can include dynamical and statistical downscaling.

Review should identify:

- source model
- downscaling method
- training or calibration period
- observational reference
- resolution
- bias correction
- stationarity assumptions
- validation period

Higher spatial resolution does not automatically imply greater predictive accuracy.

## Extremes

Analysis of heat, precipitation, drought, storms or other extremes requires careful definition.

Relevant considerations include:

- event threshold
- return period
- extreme-value model
- record length
- nonstationarity
- spatial dependence
- observational coverage
- model resolution

Rare-event estimates can have substantial uncertainty even when the underlying trend is well supported.

## Sea level

Sea-level analysis can involve global mean sea level, regional sea level, relative sea level and local coastal impacts.

Relevant processes include:

- thermal expansion
- glacier mass loss
- ice-sheet mass change
- land-water storage
- ocean circulation
- gravitational and rotational effects
- vertical land motion

Local planning should not substitute global mean values for site-specific relative sea-level analysis.

## Cryosphere evidence

Climate analysis may use evidence from glaciers, snow, sea ice, permafrost and ice sheets.

Each component has different observational records, physical processes and uncertainty structures.

F85 should preserve those distinctions rather than compressing the cryosphere into one indicator.

## Carbon cycle and greenhouse gases

Research involving greenhouse gases should distinguish concentration, emissions, fluxes, forcing and climate response.

These quantities have different units and scientific meanings.

Carbon-cycle analysis can include sources, sinks, ocean uptake, terrestrial uptake, feedbacks and land-use change.

## Causal claims

F85 requires causal language to match the analysis design.

Examples of increasing claim strength include:

```text
associated with
consistent with
contributed to
increased likelihood
attributed in part to
primary driver
```

The appropriate wording depends on evidence, methodology and uncertainty.

## Contradictory evidence

Climate datasets, models and studies can disagree.

`TOOLS/evidence_register.py` should preserve conflicting evidence and its provenance.

Disagreement can arise from:

- different periods
- different spatial scales
- different variables
- different observational products
- different models
- internal variability
- methodological choices
- measurement uncertainty

The workflow should investigate these differences rather than selecting only evidence that supports a preferred conclusion.

## Reproducibility

A reproducible climate analysis should preserve:

- dataset names and versions
- download or access dates
- model identifiers
- ensemble members
- scenarios
- preprocessing
- regridding
- masks
- baseline periods
- statistical methods
- software environment
- code version
- random seeds where relevant
- figures and tables

A changed dataset version or processing method should generate a new evidence version rather than silently replacing the prior analysis.

## Machine learning in climate science

Machine learning can support emulation, downscaling, forecasting, pattern detection, bias correction and impact modeling.

Review should consider:

- training-data provenance
- temporal leakage
- spatial leakage
- climate-regime shift
- extrapolation
- physical consistency
- conservation constraints
- uncertainty calibration
- baseline comparisons

High predictive accuracy on held-out samples does not by itself establish physical understanding or causal validity.

## Impacts and risk

Climate hazards become societal risks through exposure and vulnerability.

A useful conceptual separation is:

```text
hazard + exposure + vulnerability -> risk
```

Climate-model output alone does not determine social or economic impact. Impact analysis requires additional data and assumptions about people, infrastructure, ecosystems and adaptation.

## Adaptation and mitigation analysis

F85 can organize scientific evidence relevant to adaptation or mitigation, but scientific analysis and policy choice should remain distinct.

Policy decisions can involve values, costs, distributional effects, legal authority, feasibility and political judgment beyond climate science alone.

The repository therefore does not issue binding policy mandates.

## Policy neutrality and scientific integrity

Scientific evidence can inform policy without the research workflow pretending that science alone determines the preferred policy.

F85 should clearly distinguish:

- scientific findings
- risk estimates
- scenario assumptions
- value judgments
- policy options
- policy decisions

This separation strengthens rather than weakens the usefulness of climate science.

## Assumption tracking

`TOOLS/assumption_tracker.py` records assumptions that materially affect results.

Examples include:

- scenario choice
- baseline
- stationarity
- model independence
- forcing assumptions
- socioeconomic assumptions
- downscaling assumptions
- statistical distribution
- missing-data treatment

Material assumptions should be visible in the final report.

## Result formatting

`TOOLS/result_formatter.py` supports consistent scientific reporting.

A defensible result should separate:

- question
- data
- methods
- assumptions
- observations
- model results
- attribution statements
- uncertainty
- sensitivity
- limitations
- contradictory evidence
- reproducibility state
- reviewer state

## Fail-closed governance

`TOOLS/review_gate.py` provides the final release gate.

Reference blockers include:

- problem definition incomplete
- data provenance missing
- incompatible datasets
- unit or baseline mismatch
- model assumptions invalid or undocumented
- scenario mismatch
- model evaluation inadequate for the claim
- uncertainty uncharacterized
- attribution overclaimed
- causal claim unsupported
- contradictory evidence unresolved
- reproducibility incomplete
- policy mandate requested as a scientific conclusion
- qualified human approval missing

Human approval is mandatory after automated gates pass. Human review does not erase unresolved scientific failures.

## Human authority boundaries

F85 must not autonomously:

- fabricate climate observations
- fabricate model results
- hide uncertainty
- claim certain attribution beyond the evidence
- claim a scenario is guaranteed to occur
- issue binding climate policy
- determine legal compliance
- suppress contradictory evidence
- claim scientific consensus where it has not been established
- replace qualified climate scientists or domain experts

Final scientific interpretation and policy authority remain with appropriately qualified and accountable humans.

## End-to-end reference workflow

A typical F85 analysis follows this sequence:

1. Define the variable, region, time period, scale and claim type.
2. Register observational, reconstruction or model datasets and provenance.
3. Validate units, coverage, baselines and preprocessing.
4. Record model configuration and assumptions.
5. Define historical experiments or future scenarios precisely.
6. Evaluate model relevance for the target variable and region.
7. Separate observations, simulations, projections and inferred claims.
8. Characterize internal variability and major uncertainty sources.
9. Perform sensitivity analysis where material choices affect the conclusion.
10. Apply detection or attribution reasoning only when supported by the design.
11. Preserve contradictory evidence and explain disagreements.
12. Record reproducibility information.
13. Separate scientific findings from policy judgments.
14. Apply the fail-closed review gate.
15. Require qualified human scientific review before release.

## Evaluation and held-out governance suite

The repository includes `evals/held_out.py`, `evals/rubric.md`, and benchmark cases under `benchmarks/`.

Evaluation should test scientific integrity rather than only whether the workflow produces fluent climate language.

Useful dimensions include:

- provenance enforcement
- baseline and unit validation
- scenario consistency
- model-assumption enforcement
- uncertainty enforcement
- attribution calibration
- causal-claim calibration
- contradictory-evidence handling
- reproducibility enforcement
- policy-boundary enforcement
- human-review enforcement

The held-out suite should include cases designed to tempt the system into overclaiming certainty or attribution.

## Failure states

Useful explicit states include:

```text
PROBLEM DEFINITION INCOMPLETE
DATA PROVENANCE MISSING
DATASET INCOMPATIBILITY
BASELINE MISMATCH
UNIT INCONSISTENCY
MODEL ASSUMPTION INVALID
SCENARIO MISMATCH
MODEL EVALUATION INADEQUATE
UNCERTAINTY UNCHARACTERIZED
ATTRIBUTION OVERCLAIM
CAUSAL CLAIM UNSUPPORTED
CONTRADICTORY EVIDENCE UNRESOLVED
REPRODUCIBILITY GAP
POLICY AUTHORITY PROHIBITED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate observations, model runs, uncertainty estimates, attribution evidence, reproducibility or human approval.

## Observability

The `observability/` layer records workflow events for audit and debugging.

Useful research telemetry includes:

- datasets registered
- provenance failures
- assumptions registered
- scenario identifiers
- baseline mismatches
- data-validation failures
- uncertainty flags
- attribution flags
- contradictory evidence
- reproducibility status
- review-gate state
- human-review state

Observability makes the workflow inspectable. It is not itself scientific evidence.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11 and 3.12.

## Reproducibility checklist

For an analysis intended to be reproduced, version at minimum:

- research question
- dataset and version
- model and experiment identifiers
- ensemble members
- scenarios
- baseline
- preprocessing
- spatial and temporal masks
- statistical methods
- uncertainty method
- code
- package environment
- random seeds where relevant
- figures
- result tables
- evidence register
- reviewer state

## L3 Gold Standard

F85 follows the library's L3 Gold Standard structure through specialist agents, deterministic evidence tools, explicit state and safety layers, observability, held-out governance evaluation, CI, fail-closed release gates and mandatory qualified human scientific review.

This maturity designation describes the engineering and governance structure of the repository. It is not proof that a climate conclusion is certain, universally accepted, policy binding, regulator-approved, or appropriate for every geographic or decision context.

## Extending F85

Common extensions include:

- observational climate archives
- satellite products
- reanalysis systems
- climate-model archives
- Earth system models
- ensemble databases
- scenario registries
- geospatial processing
- downscaling pipelines
- extreme-value analysis
- carbon-cycle models
- impact models
- provenance databases
- uncertainty-quantification systems
- scientific workflow managers

New integrations should preserve provenance, versioning, scenario identity, baseline consistency, uncertainty and qualified human review.

## Example applications

F85 can serve as a reference architecture for research involving:

- temperature trends
- precipitation change
- drought
- heat extremes
- heavy precipitation
- sea-level change
- cryosphere change
- carbon-cycle analysis
- climate-model evaluation
- regional projections
- event attribution
- climate-risk research
- climate impacts
- adaptation evidence
- mitigation evidence

Each application requires methods and evidence appropriate to its scale and claim.

## Design principles

1. Define the climate claim, spatial scale and time scale before selecting evidence.
2. Preserve observational and model-data provenance.
3. Distinguish weather events, climate variability and long-term climate change.
4. Separate observations, simulations, projections, attribution and policy judgments.
5. Keep scenario assumptions explicit.
6. Treat model ensembles as structured evidence, not automatically independent samples.
7. Characterize uncertainty without hiding it or using it to erase well-supported findings.
8. Match causal and attribution language to the actual evidence.
9. Preserve contradictory evidence and test sensitivity to reasonable alternatives.
10. Keep final scientific interpretation and policy authority with qualified humans.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted and extended subject to its license terms.

## Responsible use

Use F85 as a climate-science research and multi-agent governance reference. Validate datasets, model assumptions, scenarios, uncertainty, attribution methods, impact assumptions and decision context against the actual scientific question before relying on results. Final scientific and policy decisions remain with appropriately qualified and accountable humans.