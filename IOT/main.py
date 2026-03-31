import tkinter as tk
from tkinter import scrolledtext, font
from datetime import datetime
import random
import threading
import time

class ChatbotTkinter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Assistant Virtuel - Chatbot")
        self.root.geometry("500x700")
        self.root.configure(bg='#f8f9fa')
        
        # Configuration des couleurs
        self.colors = {
            'bg': '#f8f9fa',
            'header': '#667eea',
            'user_msg': '#764ba2',
            'bot_msg': 'white',
            'text': '#333',
            'time': '#999'
        }
        
        self.setup_ui()
        self.setup_responses()
        
        # Message de bienvenue
        self.add_message("Bonjour ! Je suis votre assistant virtuel. Comment puis-je vous aider aujourd'hui ?", "bot")
        
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors['header'], height=100)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Avatar et titre
        title_label = tk.Label(header_frame, 
                              text="🤖 Assistant Virtuel", 
                              font=("Arial", 18, "bold"),
                              fg='white',
                              bg=self.colors['header'])
        title_label.pack(pady=15)
        
        status_label = tk.Label(header_frame,
                               text="En ligne • Prêt à vous aider",
                               font=("Arial", 10),
                               fg='white',
                               bg=self.colors['header'])
        status_label.pack()
        
        # Zone des messages (avec scrollbar)
        message_frame = tk.Frame(self.root, bg=self.colors['bg'])
        message_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.message_area = scrolledtext.ScrolledText(
            message_frame,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg=self.colors['bg'],
            fg=self.colors['text'],
            relief='flat',
            state='disabled'
        )
        self.message_area.pack(fill='both', expand=True)
        
        # Configurer les tags pour les messages
        self.message_area.tag_config("user_msg", 
                                     background=self.colors['user_msg'],
                                     foreground='white',
                                     justify='right',
                                     spacing3=5,
                                     font=("Arial", 11),
                                     rmargin=20,
                                     lmargin1=150,
                                     lmargin2=150)
        
        self.message_area.tag_config("bot_msg",
                                     background=self.colors['bot_msg'],
                                     foreground=self.colors['text'],
                                     justify='left',
                                     spacing3=5,
                                     font=("Arial", 11),
                                     rmargin=150,
                                     lmargin1=20,
                                     lmargin2=20)
        
        self.message_area.tag_config("time_tag",
                                     font=("Arial", 8),
                                     foreground=self.colors['time'])
        
        # Zone de saisie
        input_frame = tk.Frame(self.root, bg='white', relief='solid', bd=1)
        input_frame.pack(fill='x', padx=10, pady=10)
        
        self.input_text = tk.Text(input_frame, 
                                  height=3,
                                  font=("Arial", 11),
                                  wrap=tk.WORD,
                                  relief='flat',
                                  padx=10,
                                  pady=5)
        self.input_text.pack(side='left', fill='both', expand=True)
        
        # Bouton d'envoi
        self.send_btn = tk.Button(input_frame,
                                 text="Envoyer",
                                 command=self.send_message,
                                 font=("Arial", 10, "bold"),
                                 bg=self.colors['header'],
                                 fg='white',
                                 relief='flat',
                                 padx=15,
                                 cursor='hand2')
        self.send_btn.pack(side='right', padx=5, pady=5)
        
        # Footer avec compteur
        footer_frame = tk.Frame(self.root, bg=self.colors['bg'])
        footer_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        self.char_count = tk.Label(footer_frame,
                                   text="0/500",
                                   font=("Arial", 9),
                                   fg=self.colors['time'],
                                   bg=self.colors['bg'])
        self.char_count.pack(side='left')
        
        self.typing_indicator = tk.Label(footer_frame,
                                        text="",
                                        font=("Arial", 9, "italic"),
                                        fg=self.colors['time'],
                                        bg=self.colors['bg'])
        self.typing_indicator.pack(side='right')
        
        # Liaison des événements
        self.input_text.bind('<KeyRelease>', self.update_char_count)
        self.input_text.bind('<Return>', self.on_enter)
        
    def setup_responses(self):
        """Configure les réponses du chatbot"""
        self.responses = {
            'greetings': ['Bonjour', 'Salut', 'Hello', 'Bienvenue'],
            'help': ['Comment puis-je vous aider', 'De quoi avez-vous besoin', 'Je suis là pour vous aider'],
            'goodbye': ['Au revoir', 'À bientôt', 'Bonne journée', 'À la prochaine'],
            'thanks': ['Je vous en prie', 'Avec plaisir', 'C\'est normal', 'Heureux d\'aider']
        }
    
    def add_message(self, text, sender):
        """Ajoute un message dans la zone de discussion"""
        current_time = datetime.now().strftime("%H:%M")
        
        self.message_area.configure(state='normal')
        
        if sender == 'user':
            # Message utilisateur
            self.message_area.insert(tk.END, f"Vous  {current_time}\n", "time_tag")
            self.message_area.insert(tk.END, f"{text}\n\n", "user_msg")
        else:
            # Message bot
            self.message_area.insert(tk.END, f"Assistant  {current_time}\n", "time_tag")
            self.message_area.insert(tk.END, f"{text}\n\n", "bot_msg")
        
        self.message_area.configure(state='disabled')
        self.message_area.see(tk.END)
    
    def send_message(self):
        """Envoie le message de l'utilisateur"""
        message = self.input_text.get("1.0", tk.END).strip()
        
        if not message:
            return
        
        if len(message) > 500:
            message = message[:500]
        
        self.add_message(message, "user")
        self.input_text.delete("1.0", tk.END)
        self.update_char_count()
        
        # Simuler la frappe du bot
        self.show_typing()
        self.root.after(1000, lambda: self.process_response(message))
    
    def process_response(self, message):
        """Traite le message et génère une réponse"""
        self.hide_typing()
        response = self.generate_response(message)
        self.add_message(response, "bot")
    
    def generate_response(self, user_message):
        """Génère une réponse intelligente"""
        message = user_message.lower()
        
        # Salutations
        if any(word in message for word in ['bonjour', 'salut', 'hello', 'coucou']):
            return f"{self.get_random_response('greetings')} ! Comment allez-vous ?"
        
        # Aide
        if any(word in message for word in ['aide', 'help', 'peux-tu', 'peut-tu']):
            return f"{self.get_random_response('help')}. Je peux répondre à vos questions, discuter avec vous, ou vous aider avec diverses informations."
        
        # Remerciements
        if any(word in message for word in ['merci', 'thanks', 'cimer']):
            return self.get_random_response('thanks')
        
        # Au revoir
        if any(word in message for word in ['au revoir', 'bye', 'à plus', 'adieu']):
            return f"{self.get_random_response('goodbye')} ! N'hésitez pas à revenir si vous avez besoin d'aide."
        
        # Comment ça va
        if 'comment ça va' in message or 'ça va' in message:
            return "Je vais très bien, merci de demander ! Et vous, comment allez-vous aujourd'hui ?"
        
        # Nom du bot
        if 'nom' in message or 'appelle' in message:
            return "Je suis un assistant virtuel créé pour vous aider. Vous pouvez m'appeler simplement 'Assistant' !"
        
        # Heure
        if 'heure' in message:
            now = datetime.now()
            return f"Il est actuellement {now.strftime('%H:%M')}"
        
        # Date
        if 'date' in message:
            now = datetime.now()
            return f"Nous sommes le {now.strftime('%A %d %B %Y')}"
        
        # Blague
        if 'blague' in message:
            jokes = [
                "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau !",
                "Que dit une imprimante jet d'encre ? J'ai un problème de liquidité !",
                "Pourquoi les éléphants ne jouent-ils pas aux échecs ? Parce qu'ils ne savent pas utiliser les tours !",
                "Quel est le comble pour un électricien ? De ne pas être au courant !"
            ]
            return random.choice(jokes)
        
        # Météo
        if 'météo' in message or 'meteo' in message:
            return "Je ne peux pas encore accéder aux données météo en temps réel, mais je vous recommande de consulter une application météo pour des informations précises."
        
        # Réponse par défaut
        default_responses = ("Je suis désolé, je n'ai pas compris votre demande. Pouvez-vous reformuler ?",
                             "Je ne suis pas sûr de comprendre. Pouvez-vous préciser votre question ?",)
        
        return random.choice(default_responses)
    
    def get_random_response(self, category):
        """Retourne une réponse aléatoire d'une catégorie"""
        return random.choice(self.responses[category])
    
    def show_typing(self):
        """Affiche l'indicateur de frappe"""
        self.typing_indicator.config(text="L'assistant écrit...")
    
    def hide_typing(self):
        """Cache l'indicateur de frappe"""
        self.typing_indicator.config(text="")
    
    def update_char_count(self, event=None):
        """Met à jour le compteur de caractères"""
        text = self.input_text.get("1.0", tk.END).strip()
        count = len(text)
        self.char_count.config(text=f"{count}/500")
        
        if count >= 500:
            self.char_count.config(fg='red')
        else:
            self.char_count.config(fg=self.colors['time'])
    
    def on_enter(self, event):
        """Gère l'envoi avec la touche Entrée"""
        if not event.state & 0x1:  # Shift non enfoncé
            self.send_message()
            return "break"
    
    def run(self):
        """Lance l'application"""
        self.root.mainloop()

# Utilisation
if __name__ == "__main__":
    app = ChatbotTkinter()
    app.run()