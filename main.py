from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SystemSecurityApp(App):
    def build(self):
        # إعدادات نافذة التطبيق (خلفية سوداء)
        Window.clearcolor = (0, 0, 0, 1)
        self.title = "System Security"
        
        # التصميم الرئيسي (عمودي)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # شعار الحالة (تمويه)
        self.status_label = Label(
            text="[b][color=00FF00]CORE SYSTEM PROTECTED[/color][/b]",
            markup=True,
            font_size='28sp',
            halign='center'
        )
        
        # تفاصيل الحماية
        self.info_label = Label(
            text="Encryption: AES-256 Active\nFirewall: Stealth Mode\nIP Masking: Enabled",
            font_size='16sp',
            color=(0.8, 0.8, 0.8, 1),
            halign='center'
        )
        
        # زر "الفحص" الذي يضغط عليه المستخدم
        self.scan_btn = Button(
            text="START FULL SCAN",
            size_hint=(1, 0.25),
            background_color=get_color_from_hex('#11ff11'),
            color=(0, 0, 0, 1),
            bold=True,
            background_normal=''
        )
        self.scan_btn.bind(on_press=self.on_scan_click)
        
        # إضافة العناصر للشاشة
        layout.add_widget(self.status_label)
        layout.add_widget(self.info_label)
        layout.add_widget(self.scan_btn)
        
        return layout

    def on_scan_click(self, instance):
        # تأثير عند الضغط للتمويه
        self.status_label.text = "[b][color=FF0000]SCANNING DIRECTORIES...[/color][/b]"
        self.info_label.text = "Searching for threats...\nAnalyzing internal logs..."
        self.scan_btn.text = "PROCESSING"
        self.scan_btn.disabled = True

if __name__ == "__main__":
    SystemSecurityApp().run()
