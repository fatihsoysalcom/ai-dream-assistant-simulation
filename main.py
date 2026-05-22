import sys

def ai_assistant_response(user_input):
    """
    Simulates a basic AI assistant providing encouraging and guiding responses
    based on keywords in the user's input, reflecting the article's theme
    of AI empowering dreams and goals.
    """
    user_input_lower = user_input.lower()

    # Keywords related to dreams, goals, projects, and AI's role
    if "hayal" in user_input_lower or "dream" in user_input_lower:
        # Illustrates AI helping define and pursue dreams
        return "Harika bir hayal! Yapay zeka, hedeflerinizi netleştirmenize ve bu yolda size rehberlik etmenize yardımcı olabilir. Hayaliniz nedir?"
    elif "proje" in user_input_lower or "project" in user_input_lower:
        # Illustrates AI assisting with project planning and execution
        return "Mükemmel bir proje fikri! Yapay zeka, projenizin her aşamasında size destek olabilir; fikir aşamasından uygulamaya kadar. Başlamak için neye ihtiyacınız var?"
    elif "hedef" in user_input_lower or "goal" in user_input_lower:
        # Illustrates AI supporting goal setting and achievement
        return "Hedeflerinize ulaşmak için kararlılığınız takdire şayan. Yapay zeka, ilerlemenizi takip etmenize, engelleri aşmanıza ve motivasyonunuzu yüksek tutmanıza yardımcı olabilir."
    elif "yardım" in user_input_lower or "help" in user_input_lower or "nasıl" in user_input_lower or "how" in user_input_lower:
        # General assistance, emphasizing AI's supportive role
        return "Yapay zeka, birçok alanda size destek olabilir. Belirli bir konuda yardıma mı ihtiyacınız var, yoksa genel bir rehberlik mi arıyorsunuz?"
    elif "teşekkür" in user_input_lower or "sağ ol" in user_input_lower or "thank you" in user_input_lower:
        return "Rica ederim! Her zaman yanınızdayım. Başka nasıl yardımcı olabilirim?"
    elif "yapay zeka" in user_input_lower or "ai" in user_input_lower:
        # Direct reference to AI, explaining its empowering nature
        return "Yapay zeka, her bireyin ve kurumun potansiyelini artırmak için tasarlanmıştır. Sizin için özel olarak ne yapabilirim?"
    elif "çıkış" in user_input_lower or "exit" in user_input_lower or "quit" in user_input_lower:
        return "Görüşmek üzere! Hayallerinizi gerçekleştirmeye devam edin."
    else:
        # Default encouraging response, acting as an 'invisible assistant'
        return "Anlıyorum. Yapay zeka, düşüncelerinizi organize etmenize ve yeni fikirler keşfetmenize yardımcı olabilir. Daha fazla bilgi vermek ister misiniz?"

def main():
    print("Yapay Zeka Destekli Hayal Asistanı'na hoş geldiniz!")
    print("Hayallerinizi, projelerinizi veya hedeflerinizi benimle paylaşın.")
    print("Çıkmak için 'çıkış' yazın.")
    print("-" * 50)

    while True:
        try:
            user_input = input("Siz: ")
            if user_input.lower() in ["çıkış", "exit", "quit"]:
                print("Asistan: Görüşmek üzere! Hayallerinizi gerçekleştirmeye devam edin.")
                break
            
            # The core demonstration of the AI's 'empowering' response
            response = ai_assistant_response(user_input)
            print(f"Asistan: {response}")
            print("-" * 50)
        except EOFError:
            print("\nAsistan: Oturum sonlandırıldı. Hoşça kalın!")
            break
        except Exception as e:
            print(f"Asistan: Bir hata oluştu: {e}. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
