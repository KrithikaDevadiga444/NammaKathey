import json

def get_fact(name):
    facts = {
        'Kempe Gowda': {
            'en': 'He built 4 tall watchtowers to mark the boundaries of Bengaluru!',
            'kn': 'ಅವರು ಬೆಂಗಳೂರಿನ ಗಡಿಯನ್ನು ಗುರುತಿಸಲು 4 ಎತ್ತರದ ಕಾವಲು ಗೋಪುರಗಳನ್ನು ನಿರ್ಮಿಸಿದರು!'
        },
        'Sir M. Visvesvaraya': {
            'en': 'He was so smart that he invented automatic gates for huge dams!',
            'kn': 'ಅವರು ದೊಡ್ಡ ಅಣೆಕಟ್ಟುಗಳಿಗೆ ಸ್ವಯಂಚಾಲಿತ ಗೇಟ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯುವಷ್ಟು ಬುದ್ಧಿವಂತರಾಗಿದ್ದರು!'
        },
        'Krishnaraja Wadiyar IV': {
            'en': 'He made sure all children could go to school for free!',
            'kn': 'ಎಲ್ಲಾ ಮಕ್ಕಳು ಉಚಿತವಾಗಿ ಶಾಲೆಗೆ ಹೋಗುವುದನ್ನು ಅವರು ಖಚಿತಪಡಿಸಿದರು!'
        },
        'D. Devaraj Urs': {
            'en': 'He helped change the name of our state from Mysore to Karnataka!',
            'kn': 'ನಮ್ಮ ರಾಜ್ಯದ ಹೆಸರನ್ನು ಮೈಸೂರಿನಿಂದ ಕರ್ನಾಟಕ ಎಂದು ಬದಲಾಯಿಸಲು ಅವರು ಸಹಾಯ ಮಾಡಿದರು!'
        },
        'Rani Abbakka': {
            'en': 'She fought enemies at sea using arrows wrapped in fire!',
            'kn': 'ಅವರು ಬೆಂಕಿಯ ಬಾಣಗಳನ್ನು ಬಳಸಿ ಸಮುದ್ರದಲ್ಲಿ ಶತ್ರುಗಳೊಂದಿಗೆ ಹೋರಾಡಿದರು!'
        },
        'Karnad Sadashiva Rao': {
            'en': 'He gave away all his money just to help poor people!',
            'kn': 'ಬಡ ಜನರಿಗೆ ಸಹಾಯ ಮಾಡಲು ಅವರು ತಮ್ಮ ಎಲ್ಲಾ ಹಣವನ್ನು ದಾನ ಮಾಡಿದರು!'
        },
        'Onake Obavva': {
            'en': 'She protected a whole fort using just a wooden stick from her kitchen!',
            'kn': 'ಅವಳು ತನ್ನ ಅಡುಗೆಮನೆಯ ಮರದ ಒನಕೆಯನ್ನು ಬಳಸಿ ಇಡೀ ಕೋಟೆಯನ್ನು ರಕ್ಷಿಸಿದಳು!'
        },
        'Madakari Nayaka': {
            'en': 'He was a brave king who wore a special tiger skin to show his strength!',
            'kn': 'ಅವರು ತಮ್ಮ ಶಕ್ತಿಯನ್ನು ತೋರಿಸಲು ವಿಶೇಷ ಹುಲಿಯ ಚರ್ಮವನ್ನು ಧರಿಸಿದ್ದ ಧೈರ್ಯಶಾಲಿ ರಾಜರಾಗಿದ್ದರು!'
        },
        'Kittur Chennamma': {
            'en': 'She was one of the first queens to ride a horse and fight for freedom!',
            'kn': 'ಕುದುರೆ ಸವಾರಿ ಮಾಡಿ ಸ್ವಾತಂತ್ರ್ಯಕ್ಕಾಗಿ ಹೋರಾಡಿದ ಮೊದಲ ರಾಣಿಯರಲ್ಲಿ ಇವರೂ ಒಬ್ಬರು!'
        },
        'Sangolli Rayanna': {
            'en': 'He was a fierce warrior who fought enemies like a brave lion!',
            'kn': 'ಅವರು ಶೂರ ಸಿಂಹದಂತೆ ಶತ್ರುಗಳ ವಿರುದ್ಧ ಹೋರಾಡಿದ ಉಗ್ರ ಯೋಧರಾಗಿದ್ದರು!'
        },
        'Madhvacharya': {
            'en': 'He was very strong and could lift heavy rocks with just one hand!',
            'kn': 'ಅವರು ತುಂಬಾ ಬಲಶಾಲಿಯಾಗಿದ್ದರು ಮತ್ತು ಕೇವಲ ಒಂದು ಕೈಯಿಂದ ಭಾರವಾದ ಬಂಡೆಗಳನ್ನು ಎತ್ತಬಲ್ಲವರಾಗಿದ್ದರು!'
        },
        'Kotichennai': {
            'en': 'They were twin brothers who always fought together to protect the truth!',
            'kn': 'ಅವರು ಯಾವಾಗಲೂ ಸತ್ಯವನ್ನು ರಕ್ಷಿಸಲು ಒಟ್ಟಿಗೆ ಹೋರಾಡಿದ ಅವಳಿ ಸಹೋದರರು!'
        },
        'Kuvempu': {
            'en': 'He wrote the beautiful state song of Karnataka that we sing today!',
            'kn': 'ನಾವು ಇಂದು ಹಾಡುವ ಸುಂದರವಾದ ನಾಡಗೀತೆಯನ್ನು ಅವರು ಬರೆದಿದ್ದಾರೆ!'
        },
        'Keladi Chennamma': {
            'en': 'She was a brave queen who fought against the powerful Mughal army!',
            'kn': 'ಅವಳು ಶಕ್ತಿಶಾಲಿ ಮೊಘಲ್ ಸೈನ್ಯದ ವಿರುದ್ಧ ಹೋರಾಡಿದ ಧೈರ್ಯಶಾಲಿ ರಾಣಿ!'
        },
        'Bhimsen Joshi': {
            'en': 'He had a magical voice and practiced singing for 16 hours a day!',
            'kn': 'ಅವರು ಮಾಂತ್ರಿಕ ಧ್ವನಿಯನ್ನು ಹೊಂದಿದ್ದರು ಮತ್ತು ದಿನಕ್ಕೆ 16 ಗಂಟೆಗಳ ಕಾಲ ಹಾಡುವುದನ್ನು ಅಭ್ಯಾಸ ಮಾಡುತ್ತಿದ್ದರು!'
        },
        'Siddharoodha Swami': {
            'en': 'He traveled to many places to teach people about love and peace!',
            'kn': 'ಪ್ರೀತಿ ಮತ್ತು ಶಾಂತಿಯ ಬಗ್ಗೆ ಜನರಿಗೆ ಕಲಿಸಲು ಅವರು ಅನೇಕ ಸ್ಥಳಗಳಿಗೆ ಪ್ರಯಾಣಿಸಿದರು!'
        },
        'Rani Lakshmi Bai': {
            'en': 'She carried her baby on her back while fighting bravely in battle!',
            'kn': 'ಯುದ್ಧದಲ್ಲಿ ಧೈರ್ಯದಿಂದ ಹೋರಾಡುವಾಗ ಅವಳು ತನ್ನ ಮಗುವನ್ನು ಬೆನ್ನಿನ ಮೇಲೆ ಹೊತ್ತೊಯ್ದಳು!'
        },
        'Ibrahim Adil Shah II': {
            'en': 'He loved music so much that he played multiple instruments!',
            'kn': 'ಅವರಿಗೆ ಸಂಗೀತವೆಂದರೆ ತುಂಬಾ ಇಷ್ಟ, ಅವರು ಅನೇಕ ವಾದ್ಯಗಳನ್ನು ನುಡಿಸುತ್ತಿದ್ದರು!'
        },
        'Ali Adil Shah II': {
            'en': 'He built some of the biggest and most beautiful buildings in history!',
            'kn': 'ಅವರು ಇತಿಹಾಸದಲ್ಲಿ ಕೆಲವು ದೊಡ್ಡ ಮತ್ತು ಸುಂದರವಾದ ಕಟ್ಟಡಗಳನ್ನು ನಿರ್ಮಿಸಿದರು!'
        }
    }
    return facts.get(name, {
        'en': 'They are a famous hero from our state with many amazing stories!',
        'kn': 'ಅವರು ನಮ್ಮ ರಾಜ್ಯದ ಅನೇಕ ಅದ್ಭುತ ಕಥೆಗಳನ್ನು ಹೊಂದಿರುವ ಪ್ರಸಿದ್ಧ ನಾಯಕರು!'
    })

with open('app/src/main/assets/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for dist in data['districts']:
    for hero in dist['heroes']:
        fact = get_fact(hero['name'])
        # Keep existing facts if any, or replace. Let's just prepend our fun fact to ensure it's there
        if 'didYouKnow' not in hero:
            hero['didYouKnow'] = []
        
        # Check if already added
        exists = any(f.get('en') == fact['en'] for f in hero['didYouKnow'])
        if not exists:
            hero['didYouKnow'].insert(0, fact)

with open('app/src/main/assets/data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Updated data.json successfully!")
