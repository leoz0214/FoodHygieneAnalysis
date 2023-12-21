# Sub-Metrics Analysis - Report

## Background

The Food Hygiene Rating scheme consists of 3 sub-metrics which assesses establishments in terms of how well they perform in various aspects of food safety.

These metrics are as follows, directly from the website:
- **Hygienic food handling** - Hygienic handling of food including preparation, cooking, re-heating, cooling and storage.
- **Cleanliness and condition of facilities and building** - Cleanliness and condition of facilities and building (including having appropriate layout, ventilation, hand washing facilities and pest control) to enable good food hygiene.
- **Management of food safety** - System or checks in place to ensure that food sold or served is safe to eat, evidence that staff know about food safety, and the food safety officer has confidence that standards will be maintained in future.

For brevity, refer to these metrics as *Hygiene*, *Cleanliness* and *Management* respectively.

In terms of possible scores, unlike the overall Food Hygiene Ratings that range from 0 - 5, with 5 being the highest score (very good hygiene) and 0 being the lowest (urgent improvement necessary), for the sub-metrics, the **lower the score, the better the standards**. This means a score of 0 is ideal, indicating the standard was practically perfect.

For Hygiene and Cleanliness, the score ranges from 0 - 25, and the possible scores are multiples of 5 (0, 5, 10, 15, 20, 25).

For Management, the score ranges from 0 - 30, with the possible scores being: (0, 5, 10, 20, 30).

## Key Findings

- On average, businesses score better in **Hygiene**, and lower in Cleanliness and Management.
- Many businesses struggle with **Management** and are punished with a very low food hygiene rating.
- Generally, businesses that score well in one aspect are likely to also score well in the other two.
- But for failing businesses (Rating <= 2), many only score badly in one aspect but do fine in others.

## Deeper Analysis

### Averages

From all the records, the mean Hygiene, Cleanliness and Management scores were calculated, and the following averages were found, to two decimal places:

**Hygiene: 3.02**

Cleanliness: 3.82

Management: 3.96

This shows that on average, Hygiene is the best-scoring metric. Remmber that scores for Management can go slightly higher, up to 30, whereas Hygiene and Cleanliness only go up to 25. Therefore, Cleanliness and Management are roughly similar in standard, lower than Hygiene. It is important to note that average scores for all 3 metrics are still considered very good.

As to why Hygiene is of a higher standard, this is likely because **food handling** itself is the core aspect of food hygiene that we think about most in our daily lives, even at home. Safe food preparation, cooking and storage is a key priority for establishments, since direct unhygienic food handling practices often lead to **cross-contamination** and other dangerous situations, posing a serious threat to public health due to food poisoning. No matter how clean or well managed an establishment is, unhygienic food handling will nonetheless be very dangerous, and so, many establishments naturally perform better in this aspect of the scheme.

Cleanliness/structure involves a suitable layout, ventilation and adequate hand-washing facilities. Whilst most establishments are clean, it can be easy to accrue points due to minor issues such as a **slightly unusual layout** or a single cracked floor tile. Often, businesses in older buildings automatically struggle with this aspect due to **worsened structural condition**. **Pests** are a serious problem, and evidence of a pest infestation will result in an automatic bad score, and the severity of the infestation determines how poor the Cleanliness score is. Evidence of active pest control may lower the extent of the marking down, but the score will still not be good. Overall, it is easy for a business to have minor issues in terms of its cleanliness despite hygienic food handling. 

To score highly in Management, **documentation and records of safety procedures** must be maintained, and there must be proof that staff are trained in food safety and that the food is safe to consume. Therefore, this metric focuses less on the actual food hygiene, but more on the systems and logistics to highlight safe practices. **Lost or non-existent records** will result in a very poor result in this aspect. Some businesses may slack off in this aspect, and be penalised accordingly, despite having a hygienic, clean kitchen.

### Frequencies

Alongside averages, a further consideration is the frequency of scores for each sub-metric. The results are as follows:

Score Counts for Hygiene
- **0: 237251 (50.69%)**
- 5: 185612 (39.66%)
- 10: 39020 (8.34%)
- 15: 5504 (1.18%)
- 20: 481 (0.1%)
- 25: 133 (0.03%)

Score Counts for Cleanliness
- 0: 184806 (39.49%)
- 5: 218831 (46.76%)
- 10: 55437 (11.85%)
- 15: 7990 (1.71%)
- 20: 753 (0.16%)
- 25: 184 (0.04%)

Score Counts for Management
- 0: 186168 (39.78%)
- 5: 207875 (44.42%)
- 10: 66937 (14.3%)
- **20: 6626 (1.42%)**
- 30: 395 (0.08%)

Again, Hygiene is demonstrated to be the best performing aspect, with over half the businesses scoring perfectly. Cleanliness is lower performing than Hygiene, with less perfect scores but still somewhat few dangerously low scores.

The main insight is that there are significantly more businesses scoring very badly in **Management** than the other categories. 1.5% of businesses score 20 or worse in Management, compared to only 0.13% and 0.2% for Hygiene and Cleanliness respectively. This restricts many businesses to a rating of 0 or 1, some of which perform excellently in Hygiene and Cleanliness but fall short in terms of Management.

Explanations can be seen in the Averages section of the report.

### Correlations

The Pearson correlation for each pair of metrics has been computed. The correlations are, to three decimal places:

Hygiene and Cleanliness: 0.545

Hygiene and Management: 0.601

Cleanliness and Management: 0.539

Unsurprisingly, this shows that typically, as one metric is of a lower standard, so are the others. Hence, as one metric is of a higher standard, so are the others. This makes sense since a clean kitchen is often associated with good food handling since it shows that the business takes food safety seriously, which also correlates to robust food safety management. Nonetheless, the correlation is not very strong, so there are certainly cases where one or more aspect falls short.

A further analysis is the Pearson correlations for businesses that fail overall by attaining a Food Hygiene Rating of 2 or lower. The results to three decimal places are:

Hygiene and Cleanliness: 0.037

Hygiene and Management: 0.223

Cleanliness and Management: -0.037

Surprisingly, this demonstrates little to no correlation between the 3 metrics for low-rated businesses. The only slight correlation is between Hygiene and Management, where safer food handling may correspond to better food safety management.

This can be explained by how the rating is deduced. The final Food Hygiene Rating accounts for the **lowest scoring aspect**. If a score of 25 for Hygiene/Cleanliness or 30 for Management is accrued, this results in an automatic rating of 0. If the lowest score is 20, the rating is capped at 1, and may be 0 if the other aspects also score poorly. If the lowest score is 15, the rating is capped at 2. Hence, failure in one aspect is enough for a low overall rating.

The lack of correlation suggests that many businesses only fall short in **one** category, not dictating how they have done in other categories. As seen, lots of businesses fail in terms of Management and are automatically given a 1 or 0, and many business score well in Hygiene/Cleanliness otherwise.

This is sensible since **one failing aspect of food safety could be dangerous even if the other aspects score fine**. For example, if cross-contamination is observed, regardless of Cleanliness/Management, this is extremely dangerous and such businesses must fail. A pest infestation also warrants a fail regardless of Hygiene/Management. And lack of documentation also fails due to lack of food safety evidence, regardless of actual Hygiene/Cleanliness.