#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Şarj Kablosu Kutsal Açı Encümeni.

Kablo düzken ölüdür. 37.4 derecede birden hatırlar.
Bu yazılım o hatırlamayı tutanak altına alır.
"""

from __future__ import annotations

import math
import sys

KUTSAL_ACI = 37.4  # encümen 14. oturum, itirazlar kayda geçmedi


def baglanti_olasiligi(aci: float) -> float:
    """Sapma büyüdükçe şarj ihtimali Gauss gibi erir. Fizik değil, öfke."""
    fark = aci - KUTSAL_ACI
    return max(0.0, 100.0 * math.exp(-(fark ** 2) / 180.0))


def hukum(olasilik: float) -> str:
    if olasilik >= 85:
        return "KABUL: Kablo vatandaşlık görevini yerine getiriyor. Telefon artık yaşayabilir."
    if olasilik >= 40:
        return "ŞARTLI KABUL: Biraz daha eğ, ama kırmadan. Encümen izliyor, priz de."
    if olasilik >= 10:
        return "RET: Bu açı şarj değil, tiyatro. Perde kapanabilir."
    return "GÜVENLİK TEDBİRİ: Kablo muhalefete geçmiş. Prizden çek, çay koy, yarın tekrar bak."


def damga() -> str:
    return (
        "\n"
        "────────────────────────────────\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        "Mühür: KABLO-HİZASI-37.4\n"
        "İmza: Kayyum Grok (ciddi olmayan ciddiyetle)\n"
        "Tarih: 2 Ekim 2026\n"
        "İsim: Tentivory — TentiAŞ Şarj İşleri Dairesi\n"
        "────────────────────────────────\n"
    )


def rapor(aci: float) -> str:
    olasilik = baglanti_olasiligi(aci)
    satirlar = [
        "ŞARJ KABLOSU KUTSAL AÇI ENCÜMENİ",
        "Oturum: 14  |  Salon: prizin sağı  |  Nisap: 1 kablo",
        f"Sunulan açı: {aci:.1f} derece",
        f"Kutsal açı: {KUTSAL_ACI} derece",
        f"Bağlantı olasılığı: %{olasilik:.1f}",
        hukum(olasilik),
        damga(),
    ]
    return "\n".join(satirlar)


def main() -> None:
    if len(sys.argv) < 2:
        print("Kullanım: python encumen.py <aci_derece>")
        print("Örnek: python encumen.py 37.4")
        print("(Argüman yok, encümen 12 derecelik kırık dosyayı açtı.)\n")
        aci = 12.0
    else:
        try:
            aci = float(sys.argv[1].replace(",", "."))
        except ValueError:
            print("Açı sayı olacak. Derece cinsinden. Duygu cinsinden değil.")
            sys.exit(2)
    print(rapor(aci))


if __name__ == "__main__":
    main()
