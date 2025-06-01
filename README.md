Ce circuit de lampe LED pour culture hydroponique est conçu pour fournir un éclairage horticole de spectre complet. Il utilise un PCB en aluminium de 30 × 30 cm, équipé de 240 diodes LED réparties par couleur (5000K, 3000K, 660 nm, 730 nm), chacune contrôlable indépendamment via un microcontrôleur ESP32. L’alimentation est régulée par des drivers à courant constant compatibles PWM, permettant de moduler l’intensité lumineuse selon le stade de croissance des plantes. La structure intègre un refroidissement passif (radiateur) et des trous de fixation aux coins.

Description du fichier OpenSCAD généré
Le fichier OpenSCAD pcb_300x300_holes.scad définit un circuit imprimé (PCB) de 300 mm par 300 mm avec les caractéristiques suivantes :

Coins arrondis de rayon 5 mm pour éviter les arêtes vives lors de l’intégration dans un boîtier ou sur un radiateur.

Quatre trous de fixation de diamètre 3 mm, positionnés à 10 mm des coins, permettant une fixation stable dans un châssis, un cadre aluminium ou un support suspendu.

La forme est conçue pour l’export DXF (2D) pour la fabrication laser ou STL (3D) pour l’impression ou simulation.

Ce fichier est destiné à la réalisation d’un circuit LED horticole haute performance pour systèmes hydroponiques ou cultures indoor.


Caractéristiques d’une lampe LED optimale pour la culture de plantes
Spectre complet optimisé (Full Spectrum)
Une lampe LED de qualité doit reproduire le spectre utile à la photosynthèse (zone PAR 400–700 nm), tout en incluant :
•	5000K (blanc froid) : favorise la germination et le développement initial des plantules
•	3000K (blanc chaud) : stimule la floraison
•	660 nm (rouge profond) : augmente la productivité (photosynthèse renforcée)
•	730 nm (infrarouge lointain) : accélère la croissance (effet phytochrome)
Source scientifique :
•	Olle, M., & Viršile, A. (2013). The effects of light-emitting diode lighting on greenhouse plant growth and quality. Agricultural and Food Science.
•	Massa et al. (2008). Plant productivity in response to LED lighting. HortScience, 43(7), 1951–1956.

Puissance et PPFD requis (Photosynthetic Photon Flux Density)
Distance lampe → plante	PPFD (µmol/m²/s)	Adapté à
12 pouces (30 cm)	1081	Floraison/fleur (intensité forte)
14 pouces (35 cm)	856	Croissance végétative
18 pouces (45 cm)	640	Germination et jeunes plants
Une lampe efficace doit offrir :
•	PPFD ≥ 200–400 µmol/m²/s pour semis et jeunes pousses
•	PPFD ≥ 600–900 µmol/m²/s pour croissance végétative
•	PPFD ≥ 900–1200 µmol/m²/s pour floraison/fructification
Conseil : Utiliser un luxmètre ou PPFD meter (Apogee MQ-510, Photone App calibrée) pour vérifier la lumière au niveau des feuilles.
 
Distance d’installation recommandée (selon le stade de croissance)
Stade	Hauteur recommandée	Durée d’éclairage
Germination	60–75 cm (24–30")	18h / jour
Jeunes pousses	60 cm (24")	16h / jour
Croissance	45–60 cm (18–24")	18h / jour
Floraison	30–45 cm (12–18")	12h / jour

Protocoles spécifiques par type de plante
1. Légumes-feuilles (laitue, épinard, kale)
•	Spectre : Bleu dominant (450–470 nm)
•	PPFD : 200–400 µmol/m²/s
•	Durée : 14–18h/jour
•	Distance : 45–60 cm

2. Aromatiques (basilic, menthe, coriandre)
•	Spectre : Mix équilibré 450–660 nm
•	PPFD : 300–600 µmol/m²/s
•	Temps : 16–18h
•	Distance : 45 cm

3. Tomates / poivrons
•	Spectre : Rouge intense en floraison (660–730 nm)
•	PPFD : 700–1000 µmol/m²/s
•	Temps : 16h en croissance, 12h en floraison
•	Distance : 30–45 cm

4. Fraises et petits fruits
•	Spectre mixte : lumière rouge renforcée + IR
•	PPFD : 500–800 µmol/m²/s
•	Temps : 14–16h/jour
•	Distance : 40–50 cm

5. Fruitiers jeunes (en serre ou LED temporaire)
•	Spectre : équilibre blanc chaud + rouge
•	PPFD : 200–400 µmol/m²/s
•	Temps : 12–14h/jour
•	Distance : 60–75 cm

Astuces de terrain ("trucs de métier")
•	Toujours tester la température des feuilles (doivent être tièdes mais pas chaudes)
•	Installer des réflecteurs ou parois blanches pour maximiser le rendement lumineux
•	Coupler LED + lumière naturelle si culture sous serre (synergie + économie)
•	Ne jamais rapprocher trop une LED puissante : brûlure par excès de photons (photo-inhibition)
•	En cas de phototoxicité (bord des feuilles secs), reculer la lampe ou baisser l’intensité
•	Varier légèrement la photopériode en fin de cycle pour simuler des "saisons naturelles"

