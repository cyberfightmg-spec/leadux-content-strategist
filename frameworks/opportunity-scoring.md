# Content Opportunity Scoring

Scoring is optional and used for ordering candidates, not predicting outcomes.

Dimensions: audience_evidence, business_relevance, competitive_whitespace, freshness, historical_fit, differentiation, production_feasibility, evidence_confidence.

Each dimension is `HIGH | MEDIUM | LOW | UNKNOWN`.

Numeric sorting map: HIGH=3, MEDIUM=2, LOW=1, UNKNOWN=null. Do not impute UNKNOWN as MEDIUM.

Default weights: audience_evidence .22, business_relevance .20, competitive_whitespace .14, freshness .10, historical_fit .10, differentiation .10, production_feasibility .06, evidence_confidence .08.
