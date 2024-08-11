# AZ Reclaims

## Descripció

El mòdul `AZ_Reclaims` per a Odoo s'ha desenvolupat per a gestionar les reclamacions patrimonials associades als expedients. Aquest mòdul afegeix noves funcionalitats al mòdul d'expedients (`az_expedients`) permetent la creació, gestió i configuració de reclamacions patrimonials de manera eficient.

## Característiques Principals

- **Integració amb Expedients**: Els expedients hereten noves funcionalitats per gestionar reclamacions patrimonials associades.
- **Gestió de Reclamacions**: Possibilitat de definir i gestionar diferents tipus de reclamacions patrimonials.
- **Configuració Personalitzada**: El mòdul permet configurar quin tipus de subtipus d'expedient permet la gestió de reclamacions mitjançant la configuració en els paràmetres del sistema.

## Models Principals

El mòdul inclou els següents models:

### `expedient.py`

Aquest model hereta del model `az_expedients.expedient` i afegeix els següents camps addicionals per a gestionar reclamacions:

- `document_editor`: Selecció del redactor del document.
- `other_editor`: Text per introduir un redactor diferent al llistat predefinit.
- `amount`: Import monetari associat a la reclamació.
- `currency_id`: Moneda utilitzada per a l'import.
- `damage_state`: Estat de la reparació del dany.
- `other_state`: Estat alternatiu si l'estat no es troba entre els predefinits.
- `reclaims_ids`: Relació One2many amb el model `az_reclaims.reclaim`.
- `show_reclaims_fields`: Camp computat per mostrar o ocultar camps específics basat en el subtipo d'expedient.

### `reclaim.py`

Aquest model defineix les reclamacions específiques per a cada expedient:

- `expedient_id`: Relació Many2one amb el model `az_expedients.expedient`.
- `rtype_id`: Relació Many2one amb el model `az_reclaims.rtype`, que defineix el tipus de reclamació.
- `reference`: Referència de la reclamació.
- `description`: Descripció detallada de la reclamació.

### `rtype.py`

Aquest model defineix els diferents tipus de reclamacions que es poden gestionar:

- `name`: Nom del tipus de reclamació.
- `label`: Etiqueta utilitzada per descriure la reclamació.
- `description`: Descripció del tipus de reclamació.

### `settings.py`

Aquest model gestiona la configuració del mòdul en els paràmetres del sistema:

- `reclaim_subtype_id`: Subtipo d'expedient associat a la gestió de reclamacions.

## Dependències

Aquest mòdul depèn dels següents mòduls d'Odoo:

- `az_expedients`
- `az_documents`
- `base`

## Instal·lació

1. Descarrega o clona aquest repositori al directori `addons` del teu Odoo.
2. Asegura't que tens els mòduls `az_expedients`, `az_documents` i `base` instal·lats.
3. Reinicia el servidor Odoo.
4. Activa el mode desenvolupador i instal·la el mòdul `AZ_Reclaims` des de l'interface de Odoo.

## Configuració

Per configurar el subtipo d'expedient que permet la gestió de reclamacions patrimonials:

1. Ves a **Configuració > Paràmetres del Sistema**.
2. Busca l'entrada `az_reclaims.reclaim_subtype_id` i selecciona el subtipo d'expedient desitjat.

## Contribució

Si vols contribuir al desenvolupament d'aquest mòdul:

1. Fes un fork del repositori.
2. Crea una branca nova per a les teves modificacions.
3. Fes commit dels teus canvis.
4. Envia una sol·licitud de pull (Pull Request).

## Llicència

Aquest mòdul es distribueix sota la llicència OPL-1.

## Autoria

- Desenvolupat per: **Sofía Gràcia Mascarell**
- Correu: sofiagracia000@gmail.com
