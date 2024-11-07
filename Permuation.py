import collections
import re

# Texte chiffré - À remplacer par votre propre texte chiffré (celui-ci sert pour l'exemple)
cipher_text = """
SD GKOQDIPRSK RLP SDR CIFTQDR OGPRR O'SDR SDQPR OR
PKIQPRCRDP BSQ HRKCRPPIDP O'RXRFSPRK ORL HKGAKICCRL
RDKRAQLPKRL. F'RLP SD RDLRCNBR OR FQKFSQPL RBRFPKGDQJSRL
HRKCRPPIDP OR CIDQHSBRK ORL OGDDRRL LGSL MGKCR NQDIQKR, GS
NQPL. FRPPR CIFTQDR HRKCRP OR PKIQPRK ORL QDMGKCIPQGDL
LRBGD ORL LRJSRDFRL O'QDLPKSFPQGDL HKRORMQDQRL, IHHRBRRL
ISLLQ HKGAKICCRL.
"""

# Lettres les plus fréquentes en français pour les correspondances potentielles
# Fréquence décroissante des lettres en français : E, A, S, I, N, T, R, U, L, O, D, C, M, P, V, Q, F, B, G, H, J, X, Y, Z, K, W
freq_fr = "EASINTROULDCMPVQFBGHJXYZKW"

# Nettoyer le texte et compter les fréquences des lettres
clean_text = re.sub(r'[^A-Z]', '', cipher_text)  # Enlever les espaces et la ponctuation
cipher_freq = collections.Counter(clean_text)  # Compter les occurrences des lettres

# Trier les lettres par fréquence dans le cryptogramme
sorted_cipher_freq = [item[0] for item in cipher_freq.most_common()]

# Générer un dictionnaire de substitution initial basé sur les fréquences
substitution = {}
for i in range(len(sorted_cipher_freq)):
    substitution[sorted_cipher_freq[i]] = freq_fr[i]

# Afficher la substitution proposée
print("Substitution initiale proposée (basée sur les fréquences) :")
print(substitution)

# Fonction pour appliquer la substitution et voir le texte partiellement déchiffré
def apply_substitution(text, substitution_dict):
    return ''.join(substitution_dict.get(char, char) for char in text)

# Appliquer la substitution au texte chiffré
partially_deciphered_text = apply_substitution(cipher_text, substitution)
print("\nTexte partiellement déchiffré :")
print(partially_deciphered_text)

# Suggestions pour des digrammes et mots courts
common_digrams = ["ES", "LE", "EN", "DE", "NT", "RE"]
common_short_words = ["LE", "LA", "UN", "DE", "EN", "OU"]

# Affiner la substitution en analysant les mots de deux lettres
# TODO : Modifier la substitution jusqu'à obtenir des mots cohérents

# Fonction d'affinage (exemple d'initialisation pour peaufiner)
def refine_substitution(substitution_dict, from_letter, to_letter):
    """
    Remplace `from_letter` par `to_letter` dans le dictionnaire de substitution.
    """
    # Trouver la clé actuelle de to_letter dans la substitution et la réassigner
    current_key = next((k for k, v in substitution_dict.items() if v == to_letter), None)
    if current_key:
        substitution_dict[current_key] = from_letter  # Inverser la substitution actuelle
    substitution_dict[from_letter] = to_letter
    return substitution_dict

# Exemples d'affinage manuel, remplacez selon l'analyse que vous faites sur le texte
substitution = refine_substitution(substitution, 'S', 'U') # Commençez par essayer de remplacer 'S' par 'U'
substitution = refine_substitution(substitution, 'D', 'N') # Et de remplacer 'D' par 'N'
substitution = refine_substitution(substitution, 'P', 'T') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'O', 'D') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'G', 'O') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'R', 'E') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'C', 'M') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'N', 'B') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'B', 'L') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'L', 'S') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'J', 'Q') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'F', 'C') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'Q', 'I') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'K', 'R') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'I', 'A') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'T', 'H') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'H', 'P') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'X', 'X') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).
substitution = refine_substitution(substitution, 'A', 'G') # Ceci sert pour l'exemple à supprimer à chaque nouveau cryptogramme (cipher_text).

# Appliquer la substitution affinée et voir le texte
refined_deciphered_text = apply_substitution(cipher_text, substitution)
print("\nTexte après affinage :")
print(refined_deciphered_text)
