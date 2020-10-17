# Affcon2021 Data 

The dataset is adapted from [*Deception in Diplomacy dataset* ](https://convokit.cornell.edu/documentation/diplomacy.html). The dataset are statements taken from people's conversations during Diplomacy games played online. Diplomacy is a game about pre-World War 1 Europe. It usually has seven players: England, France, Germany, Italy, Austria-Hungary, Russia, and Turkey. In these statements, players try to form alliances to plan military campaigns and defeat each other, but things might change quickly. Each statement is a piece of a dialogue from a SENDER player to a RECEIVER player.

In this dataset, we look at how the sender player attempts to build rapport with the receiver player, in particular, when he tells the truth. 

## Dataset Fields

Fields prefixed with *affcon_* represent fields that were annotated for Affcon2021. 5 annotations were collected through Amazon Mechanical Turk for each sentence. In these fields, 1 represents a positive value, 0 represents a negative value and NA represents that the annotators did not agree on the value.

*Represents data field added for Affcon task, not present in the original dataset

|  Data Field |  Explanation |
|-------------|--------------|
| convo_id | Index of the conversation |
| msg_id | Index of the sentence in the original Diplomacy dataset |
| timestamp | Index of the sentence in the game |
| full_text | Textual content of the sentence |
| *affcon.rapport |The speaker wants to build a rapport with the receiver through "you and me" dialogue.  |
| sentence_id  | Index of the sentence  |
| speaker | The player who authored the sentence |
| reply_to | Index of the sentence to which this is a reply to (None if the sentence is not a reply) |
| speaker_intention |“Lie” if the speaker indicated this message was intended to deceive, “Truth” otherwise; this label was provided by the speaker at the time they composed the message. |
| receiver_perception | “Lie” if the receiver indicated that they perceived it as deceiving , “Truth” if the receiver indicated that the message was perceived as truthful, None if the receiver did not indicate anything; this label was provided by the receiver at the time they received the message. |
| receiver | The player whom the sentence was directed towards |
| absolute_message_index | Index of the utterance in the current conversation |
| relative_message_index | Index of the utterance in the game (same as timestamp) |
| year | Diplomacy-year in which the message was sent |
| *game_score_speaker | The difference between the Diplomacy-score the speaker and that of the receiver at the time they sent this message (game_score in the original dataset) |
| *game_score_receiver | The difference between the receiver game score and the game score (game_score + game_score_delta)|
| game_score_delta | The difference between the speaker and receiver game score|
| deception_quadrant | The type of message as defined by both how it was intended and how it was perceived. In this dataset, we focussed on "Straightforward" and "Cassandra" |
| *num_words | Number of words in the sentence | 
| *num_characters | Number of characters in the sentence |