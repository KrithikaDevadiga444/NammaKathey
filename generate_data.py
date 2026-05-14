import json
import os

data = {
    "districts": [
        {
            "id": "d1",
            "name": "Bengaluru",
            "image": "img_bengaluru",
            "heroes": [
                {
                    "id": "h1",
                    "name": "Kempe Gowda",
                    "image": "img_kempegowda",
                    "shortDesc": "Founder of Bengaluru",
                    "storyPages": [
                        {"titleEn": "Early Life", "titleKn": "ಆರಂಭಿಕ ಜೀವನ", "image": "img_kempegowda", "textEn": "Kempe Gowda was a chieftain under the Vijayanagara Empire.", "textKn": "ಕೆಂಪೇಗೌಡರು ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯದ ಅಡಿಯಲ್ಲಿ ಪಾಳೇಗಾರರಾಗಿದ್ದರು."},
                        {"titleEn": "A Dream of a City", "titleKn": "ನಗರದ ಕನಸು", "image": "img_kempegowda", "textEn": "He dreamed of a modern city with forts, lakes, and temples.", "textKn": "ಅವರು ಕೋಟೆಗಳು, ಸರೋವರಗಳು ಮತ್ತು ದೇವಾಲಯಗಳನ್ನು ಹೊಂದಿರುವ ಆಧುನಿಕ ನಗರದ ಕನಸು ಕಂಡರು."},
                        {"titleEn": "Founding Bengaluru", "titleKn": "ಬೆಂಗಳೂರಿನ ಸ್ಥಾಪನೆ", "image": "img_kempegowda", "textEn": "In 1537, he built a mud fort and founded the city of Bengaluru.", "textKn": "1537 ರಲ್ಲಿ, ಅವರು ಮಣ್ಣಿನ ಕೋಟೆಯನ್ನು ನಿರ್ಮಿಸಿದರು ಮತ್ತು ಬೆಂಗಳೂರು ನಗರವನ್ನು ಸ್ಥಾಪಿಸಿದರು."},
                        {"titleEn": "Development", "titleKn": "ಅಭಿವೃದ್ಧಿ", "image": "img_kempegowda", "textEn": "He built many lakes (Keres) for drinking water and agriculture.", "textKn": "ಕುಡಿಯುವ ನೀರು ಮತ್ತು ಕೃಷಿಗಾಗಿ ಅವರು ಅನೇಕ ಕೆರೆಗಳನ್ನು ನಿರ್ಮಿಸಿದರು."},
                        {"titleEn": "Temples", "titleKn": "ದೇವಾಲಯಗಳು", "image": "img_kempegowda", "textEn": "He built the famous Bull Temple and expanded the Gavi Gangadhareshwara Temple.", "textKn": "ಅವರು ಪ್ರಸಿದ್ಧ ಬುಲ್ ದೇವಾಲಯವನ್ನು ನಿರ್ಮಿಸಿದರು ಮತ್ತು ಗವಿ ಗಂಗಾಧರೇಶ್ವರ ದೇವಾಲಯವನ್ನು ವಿಸ್ತರಿಸಿದರು."},
                        {"titleEn": "Legacy", "titleKn": "ಪರಂಪರೆ", "image": "img_kempegowda", "textEn": "Today, Bengaluru's international airport and major bus stand are named after him.", "textKn": "ಇಂದು, ಬೆಂಗಳೂರಿನ ಅಂತರರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ ಮತ್ತು ಪ್ರಮುಖ ಬಸ್ ನಿಲ್ದಾಣಕ್ಕೆ ಅವರ ಹೆಸರನ್ನು ಇಡಲಾಗಿದೆ."}
                    ],
                    "quiz": [
                        {"questionEn": "Who founded Bengaluru?", "optionsEn": ["Kempe Gowda", "Tipu Sultan", "Krishnadevaraya", "Shivaji"], "correctAnswerIndex": 0},
                        {"questionEn": "In which year was Bengaluru founded?", "optionsEn": ["1500", "1537", "1600", "1450"], "correctAnswerIndex": 1},
                        {"questionEn": "Which empire did he serve?", "optionsEn": ["Chola", "Hoysala", "Vijayanagara", "Mughal"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:12.9716,77.5946?q=Kempegowda+Statue+Bengaluru"
                },
                {
                    "id": "h2",
                    "name": "Sir M. Visvesvaraya",
                    "image": "img_visvesvaraya",
                    "shortDesc": "Legendary Engineer and Statesman",
                    "storyPages": [
                        {"titleEn": "Early Years", "titleKn": "ಆರಂಭಿಕ ವರ್ಷಗಳು", "image": "img_visvesvaraya", "textEn": "Born in Muddenahalli, he was a brilliant student.", "textKn": "ಮುದ್ದೇನಹಳ್ಳಿಯಲ್ಲಿ ಜನಿಸಿದ ಅವರು ಪ್ರತಿಭಾವಂತ ವಿದ್ಯಾರ್ಥಿಯಾಗಿದ್ದರು."},
                        {"titleEn": "Engineering Marvels", "titleKn": "ಎಂಜಿನಿಯರಿಂಗ್ ಅದ್ಭುತಗಳು", "image": "img_visvesvaraya", "textEn": "He designed automatic weir water floodgates for dams.", "textKn": "ಅವರು ಅಣೆಕಟ್ಟುಗಳಿಗೆ ಸ್ವಯಂಚಾಲಿತ ವೀರ್ ನೀರಿನ ಪ್ರವಾಹದ ದ್ವಾರಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿದರು."},
                        {"titleEn": "KRS Dam", "titleKn": "ಕೆಆರ್ಎಸ್ ಅಣೆಕಟ್ಟು", "image": "img_visvesvaraya", "textEn": "He was the chief engineer of Krishna Raja Sagara dam in Mysuru.", "textKn": "ಮೈಸೂರಿನ ಕೃಷ್ಣರಾಜ ಸಾಗರ ಅಣೆಕಟ್ಟಿನ ಮುಖ್ಯ ಎಂಜಿನಿಯರ್ ಆಗಿದ್ದರು."},
                        {"titleEn": "Diwan of Mysore", "titleKn": "ಮೈಸೂರು ದಿವಾನ್", "image": "img_visvesvaraya", "textEn": "As Diwan, he founded many institutions including State Bank of Mysore.", "textKn": "ದಿವಾನ್ ಆಗಿ, ಸ್ಟೇಟ್ ಬ್ಯಾಂಕ್ ಆಫ್ ಮೈಸೂರು ಸೇರಿದಂತೆ ಅನೇಕ ಸಂಸ್ಥೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿದರು."},
                        {"titleEn": "Education Focus", "titleKn": "ಶಿಕ್ಷಣದ ಗಮನ", "image": "img_visvesvaraya", "textEn": "He established the Government Engineering College in Bengaluru.", "textKn": "ಅವರು ಬೆಂಗಳೂರಿನಲ್ಲಿ ಸರ್ಕಾರಿ ಎಂಜಿನಿಯರಿಂಗ್ ಕಾಲೇಜನ್ನು ಸ್ಥಾಪಿಸಿದರು."},
                        {"titleEn": "Bharat Ratna", "titleKn": "ಭಾರತ ರತ್ನ", "image": "img_visvesvaraya", "textEn": "He received the Bharat Ratna in 1955. Engineer's Day is celebrated on his birthday.", "textKn": "1955 ರಲ್ಲಿ ಭಾರತ ರತ್ನ ಪಡೆದರು. ಅವರ ಹುಟ್ಟುಹಬ್ಬದಂದು ಎಂಜಿನಿಯರ್ ದಿನವನ್ನು ಆಚರಿಸಲಾಗುತ್ತದೆ."}
                    ],
                    "quiz": [
                        {"questionEn": "Which dam did Sir MV build?", "optionsEn": ["Almatti", "KRS Dam", "Tungabhadra", "Bhakra Nangal"], "correctAnswerIndex": 1},
                        {"questionEn": "What day is celebrated on his birthday?", "optionsEn": ["Teacher's Day", "Children's Day", "Engineer's Day", "Farmer's Day"], "correctAnswerIndex": 2},
                        {"questionEn": "Which highest civilian award did he receive?", "optionsEn": ["Padma Shri", "Padma Vibhushan", "Bharat Ratna", "Param Vir Chakra"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:12.9716,77.5946?q=Visvesvaraya+Statue"
                }
            ]
        },
        {
            "id": "d2",
            "name": "Mysuru",
            "image": "img_mysuru",
            "heroes": [
                {
                    "id": "h3",
                    "name": "Krishnaraja Wadiyar IV",
                    "image": "img_krwadiyar",
                    "shortDesc": "Rajarshi of Mysore",
                    "storyPages": [
                        {"titleEn": "The Philosopher King", "titleKn": "ತತ್ವಜ್ಞಾನಿ ರಾಜ", "image": "img_krwadiyar", "textEn": "He was the 24th Maharaja of the Kingdom of Mysore.", "textKn": "ಮೈಸೂರು ಸಾಮ್ರಾಜ್ಯದ 24ನೇ ಮಹಾರಾಜರಾಗಿದ್ದರು."},
                        {"titleEn": "Golden Age", "titleKn": "ಸುವರ್ಣ ಯುಗ", "image": "img_krwadiyar", "textEn": "His rule was described as the Golden Age of Mysore.", "textKn": "ಅವರ ಆಳ್ವಿಕೆಯನ್ನು ಮೈಸೂರಿನ ಸುವರ್ಣ ಯುಗ ಎಂದು ಬಣ್ಣಿಸಲಾಗಿದೆ."},
                        {"titleEn": "Education", "titleKn": "ಶಿಕ್ಷಣ", "image": "img_krwadiyar", "textEn": "He made primary education compulsory and free.", "textKn": "ಅವರು ಪ್ರಾಥಮಿಕ ಶಿಕ್ಷಣವನ್ನು ಕಡ್ಡಾಯ ಮತ್ತು ಉಚಿತಗೊಳಿಸಿದರು."},
                        {"titleEn": "Industry", "titleKn": "ಕೈಗಾರಿಕೆ", "image": "img_krwadiyar", "textEn": "He established many industries including Mysore Sandal Soap.", "textKn": "ಮೈಸೂರು ಸ್ಯಾಂಡಲ್ ಸೋಪ್ ಸೇರಿದಂತೆ ಅನೇಕ ಕೈಗಾರಿಕೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿದರು."},
                        {"titleEn": "Women's Rights", "titleKn": "ಮಹಿಳಾ ಹಕ್ಕುಗಳು", "image": "img_krwadiyar", "textEn": "He granted voting rights to women and abolished child marriage.", "textKn": "ಮಹಿಳೆಯರಿಗೆ ಮತದಾನದ ಹಕ್ಕನ್ನು ನೀಡಿದರು ಮತ್ತು ಬಾಲ್ಯ ವಿವಾಹವನ್ನು ರದ್ದುಗೊಳಿಸಿದರು."},
                        {"titleEn": "Mahatma Gandhi's Praise", "titleKn": "ಮಹಾತ್ಮ ಗಾಂಧಿಯವರ ಹೊಗಳಿಕೆ", "image": "img_krwadiyar", "textEn": "Gandhi called him 'Rajarshi' (Saintly King).", "textKn": "ಗಾಂಧೀಜಿಯವರು ಅವರನ್ನು 'ರಾಜರ್ಷಿ' (ಸಂತ ರಾಜ) ಎಂದು ಕರೆದರು."}
                    ],
                    "quiz": [
                        {"questionEn": "Who called him 'Rajarshi'?", "optionsEn": ["Nehru", "Patel", "Mahatma Gandhi", "Bose"], "correctAnswerIndex": 2},
                        {"questionEn": "He made what kind of education free?", "optionsEn": ["College", "Primary", "University", "None"], "correctAnswerIndex": 1},
                        {"questionEn": "Which kingdom did he rule?", "optionsEn": ["Mysore", "Kittur", "Coorg", "Keladi"], "correctAnswerIndex": 0}
                    ],
                    "statueLocation": "geo:12.3051,76.6551?q=Krishnaraja+Wadiyar+Statue+Mysore"
                },
                {
                    "id": "h4",
                    "name": "D. Devaraj Urs",
                    "image": "img_devaraj",
                    "shortDesc": "Champion of Social Justice",
                    "storyPages": [
                        {"titleEn": "Early Life", "titleKn": "ಆರಂಭಿಕ ಜೀವನ", "image": "img_devaraj", "textEn": "He was born in the Hunsur taluk of Mysuru.", "textKn": "ಅವರು ಮೈಸೂರಿನ ಹುಣಸೂರು ತಾಲೂಕಿನಲ್ಲಿ ಜನಿಸಿದರು."},
                        {"titleEn": "Chief Minister", "titleKn": "ಮುಖ್ಯಮಂತ್ರಿ", "image": "img_devaraj", "textEn": "He served as the Chief Minister of Karnataka for two terms.", "textKn": "ಅವರು ಎರಡು ಅವಧಿಗೆ ಕರ್ನಾಟಕದ ಮುಖ್ಯಮಂತ್ರಿಯಾಗಿ ಸೇವೆ ಸಲ್ಲಿಸಿದರು."},
                        {"titleEn": "Land Reforms", "titleKn": "ಭೂ ಸುಧಾರಣೆಗಳು", "image": "img_devaraj", "textEn": "He implemented the 'Land to the Tiller' act, giving land to farmers.", "textKn": "ಅವರು 'ಉಳುವವನೇ ಭೂಮಿಯ ಒಡೆಯ' ಕಾಯಿದೆಯನ್ನು ಜಾರಿಗೆ ತಂದರು."},
                        {"titleEn": "Social Justice", "titleKn": "ಸಾಮಾಜಿಕ ನ್ಯಾಯ", "image": "img_devaraj", "textEn": "He championed the cause of backward classes and Dalits.", "textKn": "ಹಿಂದುಳಿದ ವರ್ಗಗಳು ಮತ್ತು ದಲಿತರ ಕಾರಣಕ್ಕಾಗಿ ಅವರು ಹೋರಾಡಿದರು."},
                        {"titleEn": "Renaming Karnataka", "titleKn": "ಕರ್ನಾಟಕ ಮರುನಾಮಕರಣ", "image": "img_devaraj", "textEn": "During his term, Mysore State was renamed as Karnataka in 1973.", "textKn": "ಅವರ ಅವಧಿಯಲ್ಲಿ, 1973 ರಲ್ಲಿ ಮೈಸೂರು ರಾಜ್ಯವನ್ನು ಕರ್ನಾಟಕ ಎಂದು ಮರುನಾಮಕರಣ ಮಾಡಲಾಯಿತು."},
                        {"titleEn": "Legacy", "titleKn": "ಪರಂಪರೆ", "image": "img_devaraj", "textEn": "He is remembered as the architect of modern social reform in the state.", "textKn": "ರಾಜ್ಯದಲ್ಲಿ ಆಧುನಿಕ ಸಾಮಾಜಿಕ ಸುಧಾರಣೆಯ ರೂವಾರಿ ಎಂದು ಅವರನ್ನು ಸ್ಮರಿಸಲಾಗುತ್ತದೆ."}
                    ],
                    "quiz": [
                        {"questionEn": "What major reform did Devaraj Urs implement?", "optionsEn": ["Education", "Land Reforms", "Space", "Military"], "correctAnswerIndex": 1},
                        {"questionEn": "When was Mysore renamed Karnataka?", "optionsEn": ["1947", "1956", "1973", "2000"], "correctAnswerIndex": 2},
                        {"questionEn": "He was the champion of which cause?", "optionsEn": ["Industry", "Social Justice", "Technology", "Art"], "correctAnswerIndex": 1}
                    ],
                    "statueLocation": "geo:12.3051,76.6551?q=Devaraj+Urs+Statue"
                }
            ]
        },
        {
            "id": "d3",
            "name": "Mangaluru",
            "image": "img_mangaluru",
            "heroes": [
                {
                    "id": "h5",
                    "name": "Rani Abbakka",
                    "image": "img_abbakka",
                    "shortDesc": "The Fearless Queen of Ullal",
                    "storyPages": [
                        {"titleEn": "The Chowta Dynasty", "titleKn": "ಚೌಟ ರಾಜವಂಶ", "image": "img_abbakka", "textEn": "Rani Abbakka belonged to the Chowta dynasty who ruled over coastal Karnataka.", "textKn": "ರಾಣಿ ಅಬ್ಬಕ್ಕ ಕರಾವಳಿ ಕರ್ನಾಟಕವನ್ನು ಆಳಿದ ಚೌಟ ರಾಜವಂಶಕ್ಕೆ ಸೇರಿದವರು."},
                        {"titleEn": "Portuguese Threat", "titleKn": "ಪೋರ್ಚುಗೀಸ್ ಬೆದರಿಕೆ", "image": "img_abbakka", "textEn": "The Portuguese wanted to capture Ullal to control the spice trade.", "textKn": "ಮಸಾಲೆ ವ್ಯಾಪಾರವನ್ನು ನಿಯಂತ್ರಿಸಲು ಪೋರ್ಚುಗೀಸರು ಉಳ್ಳಾಲವನ್ನು ವಶಪಡಿಸಿಕೊಳ್ಳಲು ಬಯಸಿದ್ದರು."},
                        {"titleEn": "Refusal to Pay Tribute", "titleKn": "ಕಪ್ಪ ಕಾಣಿಕೆ ನಿರಾಕರಣೆ", "image": "img_abbakka", "textEn": "She refused to pay tribute to the Portuguese and declared Ullal independent.", "textKn": "ಅವರು ಪೋರ್ಚುಗೀಸರಿಗೆ ಕಪ್ಪ ಕಾಣಿಕೆ ನೀಡಲು ನಿರಾಕರಿಸಿದರು ಮತ್ತು ಉಳ್ಳಾಲವನ್ನು ಸ್ವತಂತ್ರ ಎಂದು ಘೋಷಿಸಿದರು."},
                        {"titleEn": "First Battles", "titleKn": "ಮೊದಲ ಯುದ್ಧಗಳು", "image": "img_abbakka", "textEn": "She defeated the Portuguese in multiple battles in the 1550s and 1560s.", "textKn": "1550 ಮತ್ತು 1560 ರ ದಶಕಗಳಲ್ಲಿ ಅವರು ಅನೇಕ ಯುದ್ಧಗಳಲ್ಲಿ ಪೋರ್ಚುಗೀಸರನ್ನು ಸೋಲಿಸಿದರು."},
                        {"titleEn": "Agni Bana", "titleKn": "ಅಗ್ನಿ ಬಾಣ", "image": "img_abbakka", "textEn": "Her soldiers used fire arrows (Agni Bana) to burn Portuguese ships.", "textKn": "ಪೋರ್ಚುಗೀಸ್ ಹಡಗುಗಳನ್ನು ಸುಡಲು ಅವಳ ಸೈನಿಕರು ಬೆಂಕಿ ಬಾಣಗಳನ್ನು (ಅಗ್ನಿ ಬಾಣ) ಬಳಸಿದರು."},
                        {"titleEn": "First Freedom Fighter", "titleKn": "ಮೊದಲ ಸ್ವಾತಂತ್ರ್ಯ ಹೋರಾಟಗಾರ್ತಿ", "image": "img_abbakka", "textEn": "She is often considered India's first female freedom fighter.", "textKn": "ಅವರನ್ನು ಆಗಾಗ್ಗೆ ಭಾರತದ ಮೊದಲ ಮಹಿಳಾ ಸ್ವಾತಂತ್ರ್ಯ ಹೋರಾಟಗಾರ್ತಿ ಎಂದು ಪರಿಗಣಿಸಲಾಗುತ್ತದೆ."}
                    ],
                    "quiz": [
                        {"questionEn": "Which European power did Rani Abbakka fight?", "optionsEn": ["British", "French", "Portuguese", "Dutch"], "correctAnswerIndex": 2},
                        {"questionEn": "What was the capital of her kingdom?", "optionsEn": ["Mysore", "Ullal", "Kittur", "Hampi"], "correctAnswerIndex": 1},
                        {"questionEn": "What weapon did her soldiers use effectively?", "optionsEn": ["Cannons", "Guns", "Fire Arrows", "Swords"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:12.8166,74.8530?q=Rani+Abbakka+Statue+Ullal"
                },
                {
                    "id": "h6",
                    "name": "Karnad Sadashiva Rao",
                    "image": "img_karnad",
                    "shortDesc": "Freedom Fighter and Philanthropist",
                    "storyPages": [
                        {"titleEn": "Wealthy Beginnings", "titleKn": "ಶ್ರೀಮಂತ ಆರಂಭ", "image": "img_karnad", "textEn": "Born in a wealthy family in Mangaluru, he was deeply moved by poverty.", "textKn": "ಮಂಗಳೂರಿನ ಶ್ರೀಮಂತ ಕುಟುಂಬದಲ್ಲಿ ಜನಿಸಿದ ಅವರು ಬಡತನದಿಂದ ತೀವ್ರವಾಗಿ ವಿಚಲಿತರಾಗಿದ್ದರು."},
                        {"titleEn": "Following Gandhi", "titleKn": "ಗಾಂಧೀಜಿಯನ್ನು ಅನುಸರಿಸಿ", "image": "img_karnad", "textEn": "He joined the freedom struggle after meeting Mahatma Gandhi.", "textKn": "ಮಹಾತ್ಮ ಗಾಂಧಿಯನ್ನು ಭೇಟಿಯಾದ ನಂತರ ಅವರು ಸ್ವಾತಂತ್ರ್ಯ ಹೋರಾಟಕ್ಕೆ ಸೇರಿದರು."},
                        {"titleEn": "Donating Wealth", "titleKn": "ಸಂಪತ್ತು ದಾನ", "image": "img_karnad", "textEn": "He donated all his wealth to the freedom movement and the poor.", "textKn": "ಅವರು ತಮ್ಮ ಸಂಪತ್ತೆಲ್ಲವನ್ನೂ ಸ್ವಾತಂತ್ರ್ಯ ಚಳುವಳಿಗೆ ಮತ್ತು ಬಡವರಿಗೆ ದಾನ ಮಾಡಿದರು."},
                        {"titleEn": "Harijan Upliftment", "titleKn": "ಹರಿಜನ ಉದ್ದಾರ", "image": "img_karnad", "textEn": "He worked tirelessly to eradicate untouchability in the region.", "textKn": "ಪ್ರದೇಶದಲ್ಲಿ ಅಸ್ಪೃಶ್ಯತೆಯನ್ನು ನಿರ್ಮೂಲನೆ ಮಾಡಲು ಅವರು ದಣಿವರಿಯಿಲ್ಲದೆ ಕೆಲಸ ಮಾಡಿದರು."},
                        {"titleEn": "Khadi Movement", "titleKn": "ಖಾದಿ ಚಳುವಳಿ", "image": "img_karnad", "textEn": "He promoted Khadi and established weaving centers in South Kanara.", "textKn": "ಅವರು ಖಾದಿಯನ್ನು ಉತ್ತೇಜಿಸಿದರು ಮತ್ತು ದಕ್ಷಿಣ ಕನ್ನಡದಲ್ಲಿ ನೇಕಾರಿಕೆ ಕೇಂದ್ರಗಳನ್ನು ಸ್ಥಾಪಿಸಿದರು."},
                        {"titleEn": "Sacrifice", "titleKn": "ತ್ಯಾಗ", "image": "img_karnad", "textEn": "He died in poverty, having given everything to his country.", "textKn": "ತಮ್ಮ ದೇಶಕ್ಕೆ ಎಲ್ಲವನ್ನೂ ನೀಡಿ ಅವರು ಬಡತನದಲ್ಲಿ ನಿಧನರಾದರು."}
                    ],
                    "quiz": [
                        {"questionEn": "Which movement did Karnad Sadashiva Rao join?", "optionsEn": ["Quit India", "Freedom Struggle", "Sepoy Mutiny", "Bhakti"], "correctAnswerIndex": 1},
                        {"questionEn": "What did he do with his wealth?", "optionsEn": ["Kept it", "Donated it", "Invested it", "Hid it"], "correctAnswerIndex": 1},
                        {"questionEn": "Which fabric did he promote?", "optionsEn": ["Silk", "Cotton", "Khadi", "Wool"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:12.8716,74.8436?q=Karnad+Sadashiva+Rao+Statue"
                }
            ]
        },
        {
            "id": "d4",
            "name": "Chitradurga",
            "image": "img_chitradurga",
            "heroes": [
                {
                    "id": "h7",
                    "name": "Onake Obavva",
                    "image": "img_obavva",
                    "shortDesc": "Brave defender of Chitradurga Fort",
                    "storyPages": [
                        {"titleEn": "A Simple Woman", "titleKn": "ಒಬ್ಬ ಸಾಮಾನ್ಯ ಮಹಿಳೆ", "image": "img_obavva", "textEn": "Obavva was the wife of a guard at the Chitradurga Fort.", "textKn": "ಓಬವ್ವ ಚಿತ್ರದುರ್ಗ ಕೋಟೆಯ ಕಾವಲುಗಾರನ ಹೆಂಡತಿಯಾಗಿದ್ದಳು."},
                        {"titleEn": "Hyder Ali's Siege", "titleKn": "ಹೈದರ್ ಅಲಿಯ ಮುತ್ತಿಗೆ", "image": "img_obavva", "textEn": "Hyder Ali's troops were trying to enter the fort through a secret hole.", "textKn": "ಹೈದರ್ ಅಲಿಯ ಸೈನ್ಯ ರಹಸ್ಯ ರಂಧ್ರದ ಮೂಲಕ ಕೋಟೆಯನ್ನು ಪ್ರವೇಶಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿತ್ತು."},
                        {"titleEn": "Fetching Water", "titleKn": "ನೀರು ತರುವುದು", "image": "img_obavva", "textEn": "She saw the enemies while fetching water for her husband.", "textKn": "ತನ್ನ ಗಂಡನಿಗೆ ನೀರು ತರುವಾಗ ಶತ್ರುಗಳನ್ನು ನೋಡಿದಳು."},
                        {"titleEn": "The Pestle Weapon", "titleKn": "ಒನಕೆ ಆಯುಧ", "image": "img_obavva", "textEn": "She used a pestle (Onake) to strike the soldiers on the head as they entered.", "textKn": "ಒಳಬರುತ್ತಿದ್ದ ಸೈನಿಕರ ತಲೆಗೆ ಹೊಡೆಯಲು ಅವಳು ಒನಕೆಯನ್ನು ಬಳಸಿದಳು."},
                        {"titleEn": "Silent Defender", "titleKn": "ಮೂಕ ರಕ್ಷಕಿ", "image": "img_obavva", "textEn": "She quietly killed many soldiers without alerting the main enemy army.", "textKn": "ಮುಖ್ಯ ಶತ್ರು ಸೈನ್ಯವನ್ನು ಎಚ್ಚರಿಸದೆ ಅವಳು ಅನೇಕ ಸೈನಿಕರನ್ನು ಸದ್ದಿಲ್ಲದೆ ಕೊಂದಳು."},
                        {"titleEn": "Ultimate Sacrifice", "titleKn": "ಅಂತಿಮ ತ್ಯಾಗ", "image": "img_obavva", "textEn": "She died defending the fort, becoming a symbol of female courage.", "textKn": "ಮಹಿಳಾ ಧೈರ್ಯದ ಸಂಕೇತವಾಗಿ, ಕೋಟೆಯನ್ನು ರಕ್ಷಿಸುತ್ತಾ ಅವಳು ನಿಧನಳಾದಳು."}
                    ],
                    "quiz": [
                        {"questionEn": "What weapon did Obavva use?", "optionsEn": ["Sword", "Gun", "Onake", "Bow"], "correctAnswerIndex": 2},
                        {"questionEn": "Whose forces was she fighting?", "optionsEn": ["British", "Hyder Ali", "Marathas", "Mughals"], "correctAnswerIndex": 1},
                        {"questionEn": "Which fort did she defend?", "optionsEn": ["Kittur", "Mysore", "Chitradurga", "Bellary"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:14.2185,76.3983?q=Onake+Obavva+Statue"
                },
                {
                    "id": "h8",
                    "name": "Madakari Nayaka",
                    "image": "img_madakari",
                    "shortDesc": "The Last Ruler of Chitradurga",
                    "storyPages": [
                        {"titleEn": "Nayaka Dynasty", "titleKn": "ನಾಯಕ ರಾಜವಂಶ", "image": "img_madakari", "textEn": "Madakari Nayaka V was the last ruler of the Nayaka dynasty of Chitradurga.", "textKn": "ಮದಕರಿ ನಾಯಕ V ಚಿತ್ರದುರ್ಗದ ನಾಯಕ ರಾಜವಂಶದ ಕೊನೆಯ ಆಡಳಿತಗಾರನಾಗಿದ್ದನು."},
                        {"titleEn": "Military Strategy", "titleKn": "ಮಿಲಿಟರಿ ತಂತ್ರ", "image": "img_madakari", "textEn": "He was known for his military brilliance and strong fortifications.", "textKn": "ಅವನು ತನ್ನ ಮಿಲಿಟರಿ ತೇಜಸ್ಸು ಮತ್ತು ಬಲವಾದ ಕೋಟೆಗಳಿಗೆ ಹೆಸರುವಾಸಿಯಾಗಿದ್ದನು."},
                        {"titleEn": "Battles with Hyder Ali", "titleKn": "ಹೈದರ್ ಅಲಿಯೊಂದಿಗೆ ಯುದ್ಧಗಳು", "image": "img_madakari", "textEn": "He fiercely resisted Hyder Ali's expansion into his territory.", "textKn": "ತನ್ನ ಪ್ರದೇಶಕ್ಕೆ ಹೈದರ್ ಅಲಿಯ ವಿಸ್ತರಣೆಯನ್ನು ಅವನು ತೀವ್ರವಾಗಿ ವಿರೋಧಿಸಿದನು."},
                        {"titleEn": "The Long Siege", "titleKn": "ಸುದೀರ್ಘ ಮುತ್ತಿಗೆ", "image": "img_madakari", "textEn": "Chitradurga fort withstood a siege by Hyder Ali for many months.", "textKn": "ಚಿತ್ರದುರ್ಗ ಕೋಟೆ ಹಲವು ತಿಂಗಳುಗಳ ಕಾಲ ಹೈದರ್ ಅಲಿಯ ಮುತ್ತಿಗೆಯನ್ನು ತಡೆದುಕೊಂಡಿತು."},
                        {"titleEn": "Betrayal", "titleKn": "ದ್ರೋಹ", "image": "img_madakari", "textEn": "The fort fell due to betrayal by his own men.", "textKn": "ತನ್ನದೇ ಜನರ ದ್ರೋಹದಿಂದಾಗಿ ಕೋಟೆ ಪತನವಾಯಿತು."},
                        {"titleEn": "Legacy", "titleKn": "ಪರಂಪರೆ", "image": "img_madakari", "textEn": "He is remembered as a fearless warrior who fought until the end.", "textKn": "ಕೊನೆಯವರೆಗೂ ಹೋರಾಡಿದ ನಿರ್ಭೀತ ಯೋಧ ಎಂದು ಅವನನ್ನು ಸ್ಮರಿಸಲಾಗುತ್ತದೆ."}
                    ],
                    "quiz": [
                        {"questionEn": "Which dynasty did he belong to?", "optionsEn": ["Wadiyar", "Nayaka", "Chola", "Chalukya"], "correctAnswerIndex": 1},
                        {"questionEn": "Who besieged his fort?", "optionsEn": ["British", "Tipu Sultan", "Hyder Ali", "Marathas"], "correctAnswerIndex": 2},
                        {"questionEn": "Why did the fort eventually fall?", "optionsEn": ["Lack of weapons", "Betrayal", "Disease", "Earthquake"], "correctAnswerIndex": 1}
                    ],
                    "statueLocation": "geo:14.2185,76.3983?q=Madakari+Nayaka+Statue"
                }
            ]
        },
        {
            "id": "d5",
            "name": "Belagavi",
            "image": "img_belagavi",
            "heroes": [
                {
                    "id": "h9",
                    "name": "Kittur Chennamma",
                    "image": "img_chennamma",
                    "shortDesc": "Queen of Kittur",
                    "storyPages": [
                        {"titleEn": "Queen of Kittur", "titleKn": "ಕಿತ್ತೂರಿನ ರಾಣಿ", "image": "img_chennamma", "textEn": "Chennamma was the queen of the princely state of Kittur.", "textKn": "ಚೆನ್ನಮ್ಮ ಕಿತ್ತೂರು ಸಂಸ್ಥಾನದ ರಾಣಿಯಾಗಿದ್ದಳು."},
                        {"titleEn": "Doctrine of Lapse", "titleKn": "ದತ್ತು ಮಕ್ಕಳಿಗೆ ಹಕ್ಕಿಲ್ಲ", "image": "img_chennamma", "textEn": "The British tried to annex Kittur using the Doctrine of Lapse.", "textKn": "ದತ್ತು ಮಕ್ಕಳಿಗೆ ಹಕ್ಕಿಲ್ಲ ಎಂಬ ನೀತಿಯನ್ನು ಬಳಸಿ ಬ್ರಿಟಿಷರು ಕಿತ್ತೂರನ್ನು ವಶಪಡಿಸಿಕೊಳ್ಳಲು ಯತ್ನಿಸಿದರು."},
                        {"titleEn": "Defying the British", "titleKn": "ಬ್ರಿಟಿಷರನ್ನು ಧಿಕ್ಕರಿಸುವುದು", "image": "img_chennamma", "textEn": "She refused to surrender her kingdom and adopted a son.", "textKn": "ಅವಳು ತನ್ನ ರಾಜ್ಯವನ್ನು ಒಪ್ಪಿಸಲು ನಿರಾಕರಿಸಿದಳು ಮತ್ತು ಮಗನನ್ನು ದತ್ತು ತೆಗೆದುಕೊಂಡಳು."},
                        {"titleEn": "Armed Rebellion", "titleKn": "ಸಶಸ್ತ್ರ ದಂಗೆ", "image": "img_chennamma", "textEn": "In 1824, she led an armed rebellion against the East India Company.", "textKn": "1824 ರಲ್ಲಿ, ಅವಳು ಈಸ್ಟ್ ಇಂಡಿಯಾ ಕಂಪನಿಯ ವಿರುದ್ಧ ಸಶಸ್ತ್ರ ದಂಗೆಯನ್ನು ಮುನ್ನಡೆಸಿದಳು."},
                        {"titleEn": "Initial Victory", "titleKn": "ಆರಂಭಿಕ ವಿಜಯ", "image": "img_chennamma", "textEn": "She won the first battle, killing the British Collector Thackeray.", "textKn": "ಬ್ರಿಟಿಷ್ ಕಲೆಕ್ಟರ್ ಠಾಕರೆಯನ್ನು ಕೊಲ್ಲುವ ಮೂಲಕ ಅವಳು ಮೊದಲ ಯುದ್ಧವನ್ನು ಗೆದ್ದಳು."},
                        {"titleEn": "Imprisonment", "titleKn": "ಸೆರೆಮನೆ", "image": "img_chennamma", "textEn": "She was eventually captured and died in Bailhongal Fort.", "textKn": "ಕೊನೆಗೆ ಅವಳನ್ನು ಸೆರೆಹಿಡಿಯಲಾಯಿತು ಮತ್ತು ಬೈಲಹೊಂಗಲ ಕೋಟೆಯಲ್ಲಿ ನಿಧನಳಾದಳು."}
                    ],
                    "quiz": [
                        {"questionEn": "Which British policy did Chennamma fight against?", "optionsEn": ["Salt Tax", "Doctrine of Lapse", "Rowlatt Act", "Permanent Settlement"], "correctAnswerIndex": 1},
                        {"questionEn": "In which year did the rebellion take place?", "optionsEn": ["1857", "1824", "1947", "1905"], "correctAnswerIndex": 1},
                        {"questionEn": "Which British officer was killed in the first battle?", "optionsEn": ["Clive", "Hastings", "Thackeray", "Dalhousie"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:15.5562,74.7836?q=Kittur+Chennamma+Statue"
                },
                {
                    "id": "h10",
                    "name": "Sangolli Rayanna",
                    "image": "img_rayanna",
                    "shortDesc": "Brave General of Kittur",
                    "storyPages": [
                        {"titleEn": "Loyal Soldier", "titleKn": "ನಿಷ್ಠಾವಂತ ಸೈನಿಕ", "image": "img_rayanna", "textEn": "Rayanna was the army chief of the Kingdom of Kittur under Rani Chennamma.", "textKn": "ರಾಯಣ್ಣ ರಾಣಿ ಚೆನ್ನಮ್ಮನ ಅಡಿಯಲ್ಲಿ ಕಿತ್ತೂರು ಸಾಮ್ರಾಜ್ಯದ ಸೇನಾ ಮುಖ್ಯಸ್ಥನಾಗಿದ್ದನು."},
                        {"titleEn": "Guerrilla Warfare", "titleKn": "ಗೆರಿಲ್ಲಾ ಯುದ್ಧ", "image": "img_rayanna", "textEn": "After Chennamma's capture, he led a guerrilla war against the British.", "textKn": "ಚೆನ್ನಮ್ಮನನ್ನು ಸೆರೆಹಿಡಿದ ನಂತರ, ಅವನು ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ಗೆರಿಲ್ಲಾ ಯುದ್ಧವನ್ನು ಮುನ್ನಡೆಸಿದನು."},
                        {"titleEn": "Attacking British Outposts", "titleKn": "ಬ್ರಿಟಿಷ್ ಹೊರಠಾಣೆಗಳ ಮೇಲೆ ದಾಳಿ", "image": "img_rayanna", "textEn": "He attacked British offices, treasuries, and burnt their records.", "textKn": "ಅವನು ಬ್ರಿಟಿಷ್ ಕಚೇರಿಗಳು, ಖಜಾನೆಗಳ ಮೇಲೆ ದಾಳಿ ಮಾಡಿದನು ಮತ್ತು ಅವರ ದಾಖಲೆಗಳನ್ನು ಸುಟ್ಟುಹಾಕಿದನು."},
                        {"titleEn": "Support of the People", "titleKn": "ಜನರ ಬೆಂಬಲ", "image": "img_rayanna", "textEn": "He gathered a large army of local villagers to fight the British.", "textKn": "ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ಹೋರಾಡಲು ಅವನು ಸ್ಥಳೀಯ ಗ್ರಾಮಸ್ಥರ ದೊಡ್ಡ ಸೈನ್ಯವನ್ನು ಒಟ್ಟುಗೂಡಿಸಿದನು."},
                        {"titleEn": "Betrayal and Capture", "titleKn": "ದ್ರೋಹ ಮತ್ತು ಸೆರೆಮನೆ", "image": "img_rayanna", "textEn": "He was caught by the British due to betrayal by some local landlords.", "textKn": "ಕೆಲವು ಸ್ಥಳೀಯ ಜಮೀನುದಾರರ ದ್ರೋಹದಿಂದಾಗಿ ಅವನನ್ನು ಬ್ರಿಟಿಷರು ಸೆರೆಹಿಡಿದರು."},
                        {"titleEn": "Martyrdom", "titleKn": "ಹುತಾತ್ಮ", "image": "img_rayanna", "textEn": "He was hanged to death from a Banyan tree in Nandagad in 1831.", "textKn": "1831 ರಲ್ಲಿ ನಂದಗಡದಲ್ಲಿ ಆಲದ ಮರಕ್ಕೆ ನೇಣು ಹಾಕಲಾಯಿತು."}
                    ],
                    "quiz": [
                        {"questionEn": "What position did Rayanna hold in Kittur?", "optionsEn": ["King", "Army Chief", "Minister", "Spiritual Guru"], "correctAnswerIndex": 1},
                        {"questionEn": "What type of warfare did he use?", "optionsEn": ["Naval", "Trench", "Guerrilla", "Aerial"], "correctAnswerIndex": 2},
                        {"questionEn": "Where was he martyred?", "optionsEn": ["Kittur", "Mysore", "Nandagad", "Hubli"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:15.5562,74.7836?q=Sangolli+Rayanna+Statue"
                }
            ]
        },
        {
            "id": "d6",
            "name": "Udupi",
            "image": "img_udupi",
            "heroes": [
                {
                    "id": "h11",
                    "name": "Koti",
                    "image": "img_koti",
                    "shortDesc": "Legendary Hero of Tulunadu",
                    "storyPages": [
                        {"titleEn": "Twin Heroes", "titleKn": "ಅವಳಿ ವೀರರು", "image": "img_koti", "textEn": "Koti and his twin brother Chennaya are legendary heroes of Tulunadu.", "textKn": "ಕೋಟಿ ಮತ್ತು ಅವನ ಅವಳಿ ಸಹೋದರ ಚೆನ್ನಯ ತುಳುನಾಡಿನ ಪೌರಾಣಿಕ ವೀರರು."},
                        {"titleEn": "Humble Origins", "titleKn": "ವಿನಮ್ರ ಮೂಲಗಳು", "image": "img_koti", "textEn": "They belonged to the Billava community and were known for their strength.", "textKn": "ಅವರು ಬಿಲ್ಲವ ಸಮುದಾಯಕ್ಕೆ ಸೇರಿದವರು ಮತ್ತು ಅವರ ಶಕ್ತಿಗೆ ಹೆಸರುವಾಸಿಯಾಗಿದ್ದರು."},
                        {"titleEn": "Fighting Injustice", "titleKn": "ಅನ್ಯಾಯದ ವಿರುದ್ಧ ಹೋರಾಟ", "image": "img_koti", "textEn": "They fought against social injustice and oppressive local chieftains.", "textKn": "ಅವರು ಸಾಮಾಜಿಕ ಅನ್ಯಾಯ ಮತ್ತು ದಬ್ಬಾಳಿಕೆಯ ಸ್ಥಳೀಯ ಪಾಳೇಗಾರರ ವಿರುದ್ಧ ಹೋರಾಡಿದರು."},
                        {"titleEn": "Martial Arts", "titleKn": "ಮಾರ್ಷಲ್ ಆರ್ಟ್ಸ್", "image": "img_koti", "textEn": "They were masters of traditional martial arts called Garadi.", "textKn": "ಅವರು ಗರಡಿ ಎಂಬ ಸಾಂಪ್ರದಾಯಿಕ ಸಮರ ಕಲೆಗಳ ಕರಗತ ಮಾಡಿಕೊಂಡಿದ್ದರು."},
                        {"titleEn": "Epic Battles", "titleKn": "ಮಹಾಕಾವ್ಯ ಯುದ್ಧಗಳು", "image": "img_koti", "textEn": "They fought many epic battles to defend their people.", "textKn": "ತಮ್ಮ ಜನರನ್ನು ರಕ್ಷಿಸಲು ಅವರು ಅನೇಕ ಮಹಾಕಾವ್ಯ ಯುದ್ಧಗಳನ್ನು ಮಾಡಿದರು."},
                        {"titleEn": "Deification", "titleKn": "ದೈವೀಕರಣ", "image": "img_koti", "textEn": "After their heroic deaths, they were worshipped as deities (Daivas).", "textKn": "ಅವರ ವೀರ ಮರಣದ ನಂತರ, ಅವರನ್ನು ದೈವಗಳಾಗಿ (ದೈವಗಳು) ಪೂಜಿಸಲಾಯಿತು."}
                    ],
                    "quiz": [
                        {"questionEn": "Who is the twin brother of Koti?", "optionsEn": ["Rama", "Chennaya", "Laxmana", "Krishna"], "correctAnswerIndex": 1},
                        {"questionEn": "Which region do they belong to?", "optionsEn": ["Malenadu", "Tulunadu", "Bayaluseeme", "Kalyana Karnataka"], "correctAnswerIndex": 1},
                        {"questionEn": "What traditional art did they master?", "optionsEn": ["Yoga", "Garadi", "Kalaripayattu", "Karate"], "correctAnswerIndex": 1}
                    ],
                    "statueLocation": "geo:13.3408,74.7421?q=Koti+Chennaya+Statue"
                },
                {
                    "id": "h12",
                    "name": "Chennaya",
                    "image": "img_chennaya",
                    "shortDesc": "Legendary Hero of Tulunadu",
                    "storyPages": [
                        {"titleEn": "The Fierce Brother", "titleKn": "ಕ್ರೂರ ಸಹೋದರ", "image": "img_chennaya", "textEn": "Chennaya was the fiercer of the two twin heroes.", "textKn": "ಚೆನ್ನಯ ಇಬ್ಬರು ಅವಳಿ ವೀರರಲ್ಲಿ ಹೆಚ್ಚು ಉಗ್ರನಾಗಿದ್ದನು."},
                        {"titleEn": "Unbreakable Bond", "titleKn": "ಮುರಿಯಲಾಗದ ಬಂಧ", "image": "img_chennaya", "textEn": "He and Koti shared an unbreakable bond of brotherhood.", "textKn": "ಅವನು ಮತ್ತು ಕೋಟಿ ಭ್ರಾತೃತ್ವದ ಮುರಿಯಲಾಗದ ಬಂಧವನ್ನು ಹಂಚಿಕೊಂಡರು."},
                        {"titleEn": "Challenging Authority", "titleKn": "ಅಧಿಕಾರವನ್ನು ಪ್ರಶ್ನಿಸುವುದು", "image": "img_chennaya", "textEn": "They challenged the corrupt ministers of the local kingdom.", "textKn": "ಅವರು ಸ್ಥಳೀಯ ಸಾಮ್ರಾಜ್ಯದ ಭ್ರಷ್ಟ ಮಂತ್ರಿಗಳಿಗೆ ಸವಾಲು ಹಾಕಿದರು."},
                        {"titleEn": "Valor in Battle", "titleKn": "ಯುದ್ಧದಲ್ಲಿ ಶೌರ್ಯ", "image": "img_chennaya", "textEn": "Chennaya showed immense valor in the battlefield.", "textKn": "ಚೆನ್ನಯ ಯುದ್ಧಭೂಮಿಯಲ್ಲಿ ಅಪಾರ ಶೌರ್ಯವನ್ನು ಪ್ರದರ್ಶಿಸಿದನು."},
                        {"titleEn": "Tragic End", "titleKn": "ದುರಂತ ಅಂತ್ಯ", "image": "img_chennaya", "textEn": "Both brothers met a tragic but heroic end in battle.", "textKn": "ಇಬ್ಬರೂ ಸಹೋದರರು ಯುದ್ಧದಲ್ಲಿ ದುರಂತ ಆದರೆ ವೀರೋಚಿತ ಅಂತ್ಯವನ್ನು ಕಂಡರು."},
                        {"titleEn": "Paddanas", "titleKn": "ಪಾಡ್ದನಗಳು", "image": "img_chennaya", "textEn": "Their stories are sung today in traditional Tulu folk songs called Paddanas.", "textKn": "ಅವರ ಕಥೆಗಳನ್ನು ಇಂದು ಪಾಡ್ದನಗಳೆಂದು ಕರೆಯಲ್ಪಡುವ ಸಾಂಪ್ರದಾಯಿಕ ತುಳು ಜಾನಪದ ಗೀತೆಗಳಲ್ಲಿ ಹಾಡಲಾಗುತ್ತದೆ."}
                    ],
                    "quiz": [
                        {"questionEn": "What are the Tulu folk songs about them called?", "optionsEn": ["Vachanas", "Paddanas", "Kirthanas", "Dasa Sahitya"], "correctAnswerIndex": 1},
                        {"questionEn": "What was Chennaya known for?", "optionsEn": ["Poetry", "Fierceness in battle", "Trade", "Magic"], "correctAnswerIndex": 1},
                        {"questionEn": "Who did they challenge?", "optionsEn": ["British", "Corrupt ministers", "Mughals", "Marathas"], "correctAnswerIndex": 1}
                    ],
                    "statueLocation": "geo:13.3408,74.7421?q=Koti+Chennaya+Statue"
                }
            ]
        },
        {
            "id": "d7",
            "name": "Shivamogga",
            "image": "img_shivamogga",
            "heroes": [
                {
                    "id": "h13",
                    "name": "Kuvempu",
                    "image": "img_kuvempu",
                    "shortDesc": "Rashtrakavi of Karnataka",
                    "storyPages": [
                        {"titleEn": "Kuppali Venkatappa Puttappa", "titleKn": "ಕುಪ್ಪಳಿ ವೆಂಕಟಪ್ಪ ಪುಟ್ಟಪ್ಪ", "image": "img_kuvempu", "textEn": "Known by his pen name Kuvempu, he was a great Kannada poet.", "textKn": "ತಮ್ಮ ಕಾವ್ಯನಾಮ ಕುವೆಂಪು ಎಂದು ಕರೆಯಲ್ಪಡುವ ಇವರು ಶ್ರೇಷ್ಠ ಕನ್ನಡ ಕವಿ."},
                        {"titleEn": "Malnad Roots", "titleKn": "ಮಲೆನಾಡು ಬೇರುಗಳು", "image": "img_kuvempu", "textEn": "He was born in the beautiful Malnad region of Shivamogga.", "textKn": "ಇವರು ಶಿವಮೊಗ್ಗದ ಸುಂದರ ಮಲೆನಾಡು ಪ್ರದೇಶದಲ್ಲಿ ಜನಿಸಿದರು."},
                        {"titleEn": "Jnanpith Award", "titleKn": "ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ", "image": "img_kuvempu", "textEn": "He was the first Kannada writer to receive the prestigious Jnanpith Award.", "textKn": "ಪ್ರತಿಷ್ಠಿತ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ಪಡೆದ ಮೊದಲ ಕನ್ನಡ ಬರಹಗಾರ."},
                        {"titleEn": "Sri Ramayana Darshanam", "titleKn": "ಶ್ರೀ ರಾಮಾಯಣ ದರ್ಶನಂ", "image": "img_kuvempu", "textEn": "He wrote the epic poem Sri Ramayana Darshanam.", "textKn": "ಅವರು ಶ್ರೀ ರಾಮಾಯಣ ದರ್ಶನಂ ಎಂಬ ಮಹಾಕಾವ್ಯವನ್ನು ಬರೆದರು."},
                        {"titleEn": "State Anthem", "titleKn": "ನಾಡಗೀತೆ", "image": "img_kuvempu", "textEn": "He wrote the Karnataka State Anthem 'Jaya Bharata Jananiya Tanujate'.", "textKn": "ಅವರು 'ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ' ಎಂಬ ಕರ್ನಾಟಕ ನಾಡಗೀತೆಯನ್ನು ಬರೆದರು."},
                        {"titleEn": "Vishwa Manava", "titleKn": "ವಿಶ್ವ ಮಾನವ", "image": "img_kuvempu", "textEn": "He promoted the concept of 'Vishwa Manava' or Universal Citizen.", "textKn": "ಅವರು 'ವಿಶ್ವ ಮಾನವ' ಅಥವಾ ಸಾರ್ವತ್ರಿಕ ನಾಗರಿಕ ಎಂಬ ಪರಿಕಲ್ಪನೆಯನ್ನು ಉತ್ತೇಜಿಸಿದರು."}
                    ],
                    "quiz": [
                        {"questionEn": "What is Kuvempu's famous epic poem?", "optionsEn": ["Mahabharata", "Sri Ramayana Darshanam", "Mankuthimmana Kagga", "Kavirajamarga"], "correctAnswerIndex": 1},
                        {"questionEn": "Which award was he the first Kannada writer to win?", "optionsEn": ["Nobel", "Jnanpith", "Booker", "Pulitzer"], "correctAnswerIndex": 1},
                        {"questionEn": "He wrote the state anthem of which state?", "optionsEn": ["Kerala", "Tamil Nadu", "Karnataka", "Maharashtra"], "correctAnswerIndex": 2}
                    ],
                    "statueLocation": "geo:13.6263,75.1466?q=Kuvempu+Kavishaila"
                },
                {
                    "id": "h14",
                    "name": "Keladi Chennamma",
                    "image": "img_keladi",
                    "shortDesc": "The Valorous Queen",
                    "storyPages": [
                        {"titleEn": "Queen of Keladi", "titleKn": "ಕೆಳದಿಯ ರಾಣಿ", "image": "img_keladi", "textEn": "Chennamma was the queen of the Keladi Kingdom in Karnataka.", "textKn": "ಚೆನ್ನಮ್ಮ ಕರ್ನಾಟಕದ ಕೆಳದಿ ಸಾಮ್ರಾಜ್ಯದ ರಾಣಿಯಾಗಿದ್ದಳು."},
                        {"titleEn": "Rule of Prosperity", "titleKn": "ಸಮೃದ್ಧಿಯ ಆಳ್ವಿಕೆ", "image": "img_keladi", "textEn": "She ruled for 25 years, bringing peace and prosperity.", "textKn": "ಅವಳು 25 ವರ್ಷಗಳ ಕಾಲ ಆಳ್ವಿಕೆ ನಡೆಸಿದಳು, ಶಾಂತಿ ಮತ್ತು ಸಮೃದ್ಧಿಯನ್ನು ತಂದಳು."},
                        {"titleEn": "Sheltering Rajaram", "titleKn": "ರಾಜಾರಾಮ್‌ಗೆ ಆಶ್ರಯ", "image": "img_keladi", "textEn": "She bravely provided shelter to Rajaram, son of Shivaji, who was fleeing from the Mughals.", "textKn": "ಮೊಘಲರಿಂದ ಪಲಾಯನ ಮಾಡುತ್ತಿದ್ದ ಶಿವಾಜಿಯ ಮಗ ರಾಜಾರಾಮ್‌ಗೆ ಅವಳು ಧೈರ್ಯದಿಂದ ಆಶ್ರಯ ನೀಡಿದಳು."},
                        {"titleEn": "Defeating Aurangzeb", "titleKn": "ಔರಂಗಜೇಬನ ಸೋಲು", "image": "img_keladi", "textEn": "She successfully repelled the mighty army of the Mughal Emperor Aurangzeb.", "textKn": "ಮೊಘಲ್ ಚಕ್ರವರ್ತಿ ಔರಂಗಜೇಬನ ಪ್ರಬಲ ಸೈನ್ಯವನ್ನು ಅವಳು ಯಶಸ್ವಿಯಾಗಿ ಹಿಮ್ಮೆಟ್ಟಿಸಿದಳು."},
                        {"titleEn": "Treaty", "titleKn": "ಒಪ್ಪಂದ", "image": "img_keladi", "textEn": "Aurangzeb was forced to sign a treaty recognizing her sovereignty.", "textKn": "ತನ್ನ ಸಾರ್ವಭೌಮತ್ವವನ್ನು ಗುರುತಿಸುವ ಒಪ್ಪಂದಕ್ಕೆ ಸಹಿ ಹಾಕುವಂತೆ ಔರಂಗಜೇಬನಿಗೆ ಒತ್ತಾಯಿಸಲಾಯಿತು."},
                        {"titleEn": "Symbol of Courage", "titleKn": "ಧೈರ್ಯದ ಸಂಕೇತ", "image": "img_keladi", "textEn": "She is celebrated as a symbol of female valor and independence.", "textKn": "ಅವಳನ್ನು ಮಹಿಳಾ ಶೌರ್ಯ ಮತ್ತು ಸ್ವಾತಂತ್ರ್ಯದ ಸಂಕೇತವಾಗಿ ಆಚರಿಸಲಾಗುತ್ತದೆ."}
                    ],
                    "quiz": [
                        {"questionEn": "Which Mughal Emperor did she defeat?", "optionsEn": ["Akbar", "Shah Jahan", "Aurangzeb", "Babur"], "correctAnswerIndex": 2},
                        {"questionEn": "Whom did she provide shelter to?", "optionsEn": ["Shivaji", "Rajaram", "Sambhaji", "Peshwa"], "correctAnswerIndex": 1},
                        {"questionEn": "Which kingdom did she rule?", "optionsEn": ["Keladi", "Kittur", "Mysore", "Bijapur"], "correctAnswerIndex": 0}
                    ],
                    "statueLocation": "geo:14.2185,76.3983?q=Keladi+Chennamma+Statue"
                }
            ]
        }
    ]
}

with open("app/src/main/assets/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
