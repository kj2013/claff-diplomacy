# CL-Aff Shared Task: Diplomacy (Deadline Nov 2020)

Corpus and annotations for the CL-Aff Shared Task - Diplomacy - from the National University of Singapore

A part of the AffCon Workshop @ AAAI 2021 for Affect in Collaborative Creation

We introduce the CLAff-Diplomacy dataset this year, which examines the role of affect in inter- and intra-team trust. It builds on the Diplomacy dataset (Peskov, Cheng, Elgohary, Barrow, Danescu-Niculescu-Mizil, & Boyd-Graber, 2020; Niculae, Kumar, Boyd-Graber, & Danescu-Niculescu-Mizil, 2015 ) with additional annotations, and derived outcomes related to collaboration. This dataset is in English.

**Registration Deadline Nov 4, 2020** 

# LICENSE

Our dataset is available under CC BY 4.0 license (https://creativecommons.org/licenses/by/4.0/)

## The Tasks

GIVEN: Utterances by players in an online game called Diplomacy, labeled for their rapport characteristics.

TASK 1 : Semi-supervised learning task: Predict labels for whether the speaker is building interpersonal rapport, based on a small labeled and large unlabeled training data.

TASK 2: Unsupervised task: Explore the relationship between rapport and the receiver's trust labels.

## Corpus details 

**Unlabeled training set** : RELEASED! The Diplomacy dataset from (http://vene.ro/betrayal/)

**Labeled training set** : RELEASED! 9,858 sentences labeled for indicators of rapport-building!

**Test set:** ETA Nov 20, 2020. Only released to registered participants.



Five annotators were asked to indicate the overall presence of rapport, and then the presence of its subcategories.
For the purpose of this task, only the overall score for rapport is being used in the task, where the overall percentage agreement was 75.8%. Annotations for the subcategories were used as an additional filter to denoise the annotations and identify false positives. A final check was performed by the Shared Task organizer to ensure data quality.

Even so, errors may have slipped in. In the spirit of a Shared Task, we'd appreciate any support to help us further clean up the annotations. Thank you!.




## Label descriptions

Check out the annotation instructions under /docs/.



## Git Contents

This is the open repository for Affect Understanding in Text and Annotations contributed to the public through the collaboration between the National University of Singapore and Adobe Research India.


    ./README.md :
 
This file.


    ./FAQ2021 :
	
To be added, will have frequently asked questions including updates to the corpus.


    ./docs/annotation_instructions.html :
  
Annotation instructions for each of the labels

  

    ./docs/annotation_task.html :
  
The actual AMT task


    ./data/unlabeled training data :
  
Directory containing unlabeled data pertaining to the training and the test sets.


    ./data/labeled training data
  
Added! Directory containing the training set.


    TEST DATA?

Will be shared with the participants who register.



## Organisers' Contacts

The system outputs from the test set should be submitted to the task organizers, for the collation of the final results to be presented at the workshop.

If you have any questions regarding the workshop scope or need further information, please do not hesitate to send an e-mail: 

Niyati, nchhaya [AT] adobe.com

Kokil, jaidka [AT] nus.edu.sg







## Check out the FAQ! 

Please "WATCH" this repository! We may be pushing more updates in the following weeks.
After the Shared Task, we also plan to further enrich this data, with more annotations, meta-features and trained classifiers to aid with downstream applications.

If you use the data and publish, please let us know and cite the original Diplomacy dataset papers, as well as the CL-Aff overview paper (TBA):


Niculae, V., Kumar, S., Boyd-Graber, J., & Danescu-Niculescu-Mizil, C. (2015, July). Linguistic Harbingers of Betrayal: A Case Study on an Online Strategy Game. In Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) (pp. 1650-1659).

Peskov, D., Cheng, B., Elgohary, A., Barrow, J., Danescu-Niculescu-Mizil, C., & Boyd-Graber, J. (2020). It Takes Two to Lie: One to Lie, and One to Listen. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics.

## Acknowledgement

We're grateful to Cristian Danescu-Niculescu-Mizil and the team of coauthors (Peskov, Cheng, Elgohary, Barrow, Danescu-Niculescu-Mizil, & Boyd-Graber, 2020; Niculae, Kumar, Boyd-Graber, & Danescu-Niculescu-Mizil, 2015 ) for the permission to use the original data behind this task. Thank you!


## Organizers

Kokil Jaidka, National University of Singapore

Lynnette Ng, Carnegie Mellon University

Niyati Chhaya, Big Data Experience Lab, Adobe Research

Check out the Workshop and Shared Task website: <a>https://sites.google.com/view/affcon2021/home</a>



