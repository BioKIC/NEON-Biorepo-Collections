# NEON-Biorepo-Collections ![Build Status](https://travis-ci.com/BioKIC/NEON-Biorepo-Collections.svg?branch=api)

Simple, static API exposing information on the [NEON Biorepository Portal](https://biorepo.neonscience.org/) collections.

Current version: 0.0 (updated April 2020)

Changes can be implemented at any time. Most current information, as well as archived versions of the data will be available.

## The NEON Biorepository

The [NEON Biorepository](https://biorepo.neonscience.org/) is part of the [Biodiversity Knowledge Integration Center at Arizona State University](https://biokic.asu.edu/), located in Tempe, Arizona, USA.

The Biorepository missions include storing, curating and managing samples and data associated with samples collected by [The National Ecological Observatory Network](https://www.neonscience.org/).

The collection information available in this repository pertains to NEON-collected samples that are physically housed at the Biorepository at ASU and elsewhere, and to the associated data available at the [Biorepository Data Portal](https://biorepo.neonscience.org/).

## API
---------

### Get a full list of collections with specimens deposited at the NEON Biorepository at Arizona State University

Use `https://biokic.github.io/NEON-Biorepo-Collections/api/v0/collections/`

### Get a full list of external collections with data published in portal (both NEON and non-NEON)

Use `https://biokic.github.io/NEON-Biorepo-Collections/api/v0/collections/external`


## CSV Data
-----------

Explore or download full lists from [data directory](./data). The most current version of each dataset will be dated in the root, and archived versions will be found in the [archive subdirectory](./data/archive/) subdirectory.

