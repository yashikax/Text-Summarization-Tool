import tkinter as tk
from tkinter import filedialog, messagebox
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

class TextSummarizer:
    def __init__(self, root):
        self.root = root
        self.root.title('Text Summarizer')

        # Create input and output frames
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.LEFT, padx=10, pady=10)

        output_frame = tk.Frame(self.root)
        output_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Create input text area with label
        input_label = tk.Label(input_frame, text="Paste or write the text you want to summarize here:")
        input_label.pack()
        self.input_text = tk.Text(input_frame, width=40, height=20)
        self.input_text.pack()

        # Create output text area with label
        output_label = tk.Label(output_frame, text="Summary will appear here:")
        output_label.pack()
        self.output_text = tk.Text(output_frame, width=40, height=20)
        self.output_text.pack()

        # Create summarize button
        self.summarize_button = tk.Button(self.root, text='Summarize', command=self.summarize_text)
        self.summarize_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Create upload button
        self.upload_button = tk.Button(self.root, text='Upload File', command=self.upload_file)
        self.upload_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Create summary length slider
        self.summary_length_slider = tk.Scale(self.root, from_=1, to=10, orient=tk.HORIZONTAL, label='Summary Length', length=200)
        self.summary_length_slider.pack(side=tk.BOTTOM, padx=10, pady=10)

    def summarize_text(self):
        # Get input text
        input_text = self.input_text.get('1.0', tk.END)

        # Check if input text is empty
        if not input_text.strip():
            messagebox.showerror('Error', 'Please paste or upload text to summarize.')
            return

        # Tokenize text
        words = word_tokenize(input_text)
        sentences = sent_tokenize(input_text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word.lower() not in stop_words]

        # Calculate word frequencies
        freq_dist = FreqDist(words)

        # Rank sentences by word frequency
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence):
                if word.lower() in freq_dist:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_dist[word]

        # Get top-ranked sentences
        top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

        # Get summary length from slider
        summary_length = int(self.summary_length_slider.get())

        # Select top sentences based on summary length
        top_sentences = top_sentences[:summary_length]

        # Create summary text
        summary_text = ' '.join([sentence for sentence, score in top_sentences])

        # Display summary text
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', summary_text)

    def upload_file(self):
        # Open file dialog to select file
        file_path = filedialog.askopenfilename(title='Select File', filetypes=[('Text Files', '*.txt')])

        # Check if file is selected
        if file_path:
            try:
                # Read file contents
                with open(file_path, 'r') as file:
                    input_text = file.read()

                # Display file contents in input text area
                self.input_text.delete('1.0', tk.END)
                self.input_text.insert('1.0', input_text)
            except FileNotFoundError:
                messagebox.showerror('Error', 'File not found.')

if __name__ == '__main__':
    root = tk.Tk()
    app = TextSummarizer(root)
    root.mainloop()