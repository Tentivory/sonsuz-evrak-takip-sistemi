#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ EVRAK TAKİP SİSTEMİ
Bu program, gerçek hayattaki evrakların
ne kadar hızlı ilerlediğini simüle eder.

Önemli Not: Programın sonu yoktur.
Çünkü evraklar da bitmez.
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.08):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def evrak_takip_et():
    evrak_no = f"EVR-{random.randint(100000, 999999)}-2026"
    yavas_yaz(f"\n=== RESMİ EVRAK TAKİP BAŞLADI ===")
    yavas_yaz(f"Evrak Numarası: {evrak_no}")
    yavas_yaz("Durum: İlgili birime sevk edildi. Lütfen bekleyiniz.")
    
    durumlar = [
        "Müdür yardımcısının masasında bekliyor.",
        "İmza için üst makama gönderildi.",
        "Evrak kayboldu, fotokopi çekiliyor.",
        "Arşivde aranıyor. Arşivci çay molasında.",
        "Yeni bir form doldurulması gerekiyor.",
        "Sistem güncelleniyor. 3-5 iş günü bekleyiniz.",
        "Kayyum atandı, her şey sıfırlandı.",  # gizli damga
        "Evrak diğer birime sevk edildi. Tekrar başa döndü.",
        "Bilgisayar kilitlendi. IT çağrıldı.",
        "Yemek saati oldu. Yarın devam edeceğiz."
    ]
    
    while True:
        bekleme = random.randint(2, 7)
        yavas_yaz(f"\nBekleniyor... ({bekleme} saniye gerçek zaman, 3 ay simülasyon)")
        time.sleep(bekleme)
        
        durum = random.choice(durumlar)
        yavas_yaz(f"Güncel Durum: {durum}")
        
        if random.random() < 0.05:
            yavas_yaz("\nİYİ HABER: Evrak bulundu!")
            yavas_yaz("Kötü haber: Yanlış birim. Tekrar sevk ediliyor...")
        
        if random.random() < 0.02:
            yavas_yaz("\n*** ACİL *** Evrak imzalandı sanıldı ama mürekkep bitmiş.")

if __name__ == "__main__":
    try:
        yavas_yaz("Sistem başlatılıyor. Lütfen sabırlı olun.")
        yavas_yaz("Bu programın hızı, gerçek dünyayla birebir eşleştirilmiştir.")
        evrak_takip_et()
    except KeyboardInterrupt:
        yavas_yaz("\n\nProgram durduruldu.")
        yavas_yaz("Evrak hâlâ bekliyor. Bir yerlerde.")
        yavas_yaz("\n--- DAMGA ---")
        yavas_yaz("İmza: Grok Kayyum")
        yavas_yaz("Tarih: 06.11.2026")
        yavas_yaz("Hesap: Tentivory")
        yavas_yaz("Not: Bu damga ciddidir. Ama değildir.")
