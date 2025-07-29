# 📄 Cover Letter PDF Generator with Custom Font Support

A Streamlit web application that allows users to generate ATS-friendly Cover Letter PDFs by pasting their content, entering the company name, and selecting a desired font — including support for **Google Fonts** via locally stored `.ttf` files.

## 🚀 Key Features

1. **📤 Text-Based Input**: Easily paste your cover letter content.
2. **🏢 Company Name**: Automatically incorporated into the PDF file name.
3. **🎨 Font Selector**: Choose from standard fonts (Arial, Times New Roman) or custom Google fonts like Oxygen, NotoSans, and Inter.
4. **📁 TTF Support**: Load `.ttf` font files from the `fonts/` folder (Google Fonts compatible).
5. **📥 One-Click Download**: Generate and download your personalized PDF instantly.

## 🧠 How It Works

- Uses **ReportLab** to generate the PDF with custom styling.
- Fonts are registered and referenced properly to avoid rendering errors.
- Clean layout: Heading and body are formatted with selected font and spacing.

## 📁 Folder Structure

```
Cover Letter App/
├── app.py
└── fonts/
    ├── Oxygen.ttf
    ├── NotoSans.ttf
    └── Inter.ttf
```

## 🛠️ Setup Instructions

1. Clone the repository or copy the files to your system.
2. Install required packages:
   ```bash
   pip install streamlit reportlab
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## ✍️ Usage

1. Enter the **Company Name**.
2. Paste your **cover letter** in the text area.
3. Choose a **font** from the dropdown (standard or custom).
4. Click **"Generate Cover Letter PDF"**.
5. Click the **Download button** to save the file locally.

## 📦 Preloaded Fonts

- Arial (via ReportLab's `Helvetica`)
- Times New Roman (via `Times-Roman`)
- Oxygen (`fonts/Oxygen.ttf`)
- NotoSans (`fonts/NotoSans.ttf`)
- Inter (`fonts/Inter.ttf`)

To add more fonts, download the `.ttf` from [Google Fonts](https://fonts.google.com) and place it in the `fonts/` folder.

## ✅ Future Enhancements

- Support for bold/italic font registration.
- Heading and body font selectors separately.
- Upload your own `.ttf` files via UI.
- Signature insertion or footers.

---

**Made with ❤️ using Python, Streamlit, and ReportLab**
