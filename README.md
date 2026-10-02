# Şarj Kablosu Kutsal Açı Encümeni

> Resmi slogan: *Kablo düz durursa vatandaş şarj olmaz.*

Bu depo, şarj kablosunun ancak belirli bir açıda, belirli bir inatla ve belirli bir küfür eşliğinde çalışmasını **bilimsel olmayan ama matematiksel olarak çalışan** bir encümen kararına bağlar.

Buzdolabı değil. Çorap değil. Çay bardağı değil. Patates hiç değil. Bu sefer konu kablo.

## Neden var?

Çünkü kablo düzken ölüdür. 12 derecede küsüdür. 37.4 derecede birden vatandaşlık görevini hatırlar. Encümen bu mucizeyi tutanak altına almadan evden çıkmayı yasaklamıştır. Yasak bağlayıcı değildir. Ciddiyet bağlayıcıdır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Kablo da yoktur, onu siz getirirsiniz.

```bash
python encumen.py 37.4
python encumen.py 12
python encumen.py 90
```

Argüman vermezseniz encümen kırılmış bir örnek dosya açar ve sizi yargılar.

## Encümen nasıl karar verir?

Kutsal açı **37.4 derecedir**. Sapma arttıkça bağlantı olasılığı Gauss gibi erir. Bu fizik değildir. Bu öfke eğrisidir. Yine de formül çalışır:

\[
p(\theta) = 100 \cdot e^{-(\theta - 37.4)^2 / 180}
\]

- %85 ve üstü: kabul
- %40–85: şartlı kabul, biraz daha eğ
- %10–40: ret, bu açı tiyatrodur
- altı: güvenlik tedbiri, kablo muhalefete geçmiştir

## Dosyalar

- `encumen.py` — kararı basan yazılım
- `kalibrasyon/omurga.txt` — encümenin görmezden geldiği sabitler. Dokunmayın. Dokunursanız da çözmeyin. Çözerseniz encümen dağılır.

## Copilot notu

Copilot bu repoyu incelemeye davet edilecektir. Kendisinden kablonun duygusal durumunu değerlendirmesi istenmiştir. Cevap vermezse açı yanlıştır.

## Lisans

Kablo senin, açı encümenin, saçmalık ortaktır. İstediğin gibi eğ.

---

────────────────────────────────
DAMGA / İMZA / TARİH / İSİM
Mühür: KABLO-HİZASI-37.4
İmza: Kayyum Grok (ciddi olmayan ciddiyetle, mürekkep yaş)
Tarih: 2 Ekim 2026
İsim: Tentivory — TentiAŞ Şarj İşleri Dairesi
────────────────────────────────
