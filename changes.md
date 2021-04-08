## Data changes

# 2021-04, v1.0

- Main "External" category now divided in two:

1. "Additional NEON Collections": collections belonging to NEON, but hosted in different institutions other than ASU
2. "Other Collections from NEON sites": collections not related to NEON, but with samples collected in the same localities that NEON has

# 2020-07, v1.0

- Additional external collections
- Minor character encoding fixes

# 2020-06, v1.0

- Minor spelling fixes
- Availability fixes

## 2020-06, v0.1

### All Collections

- Collections with `collid` in `[7,8,9]` moved to category `Plants`
- Changed spelling of Algae collections
- Added field `neontheme` with options:

  - Atmosphere
  - Atmosphere, Land Cover & Processes
  - Biogeochemistry, Land Cover & Processes
  - Biogeochemistry, Organisms, Populations, and Communities
  - Organisms, Populations, and Communities

- Added boolean field `available` to display information about availability of samples at ASU

- Removed field `preservation` (Previously parsed from `fullname`)
- Added field `sampletype` with options:

  - DNA Sample
  - Dry Sample
  - Environmental Sample
  - Fluid-Preserved Sample1
  - Frozen Sample
  - Slide-Mounted Sample
  - Tissue or Fecal Sample

- Broke `taxon` field in two fields.
- Added `highertaxon` field with options:

  - Aquatic Invertebrates
    Aquatic plants, bryophytes, lichens, and macroalgae
  - Environmental
  - Microbes
  - Periphyton, seston, and phytoplankton
  - Terrestrial Invertebrates
  - Terrestrial Plants
  - Vertebrates

- Added `lowertaxon` field with options:
  - Aquatic Plant, Bryophyte, and Lichen
  - Benthic Macroinvertebrates
  - Benthic Microbes
  - Carabids
  - Fishes
  - Herptiles
  - Mammals
  - Mosquitoes
  - Other Invertebrates
  - Soil Microbes
  - Surface Water Microbes
  - Ticks
  - Zooplankton

Notes: CSV file was manually produced, as database changes aren't yet in place. JSON file was produced with Python, but arrays were manually encoded.
