


###---------------------------
### PLAYER CHARACTERS
###---------------------------

# The 4 roles and their associated die
roles = {
    'Expert' : 'd4',
    'Vanguard' : 'd6',
    'Fighter' : 'd8',
    'Tank' : 'd10'
}

# Giant fancy nested dictionary that defines specific edges and traits for specific classes.
character_classes = {
    'The Renegade': {
        'flavor text': 'You have turned your back on the Killstar Republick.\n         As a RENEGADE you are considered a TRAITOR by your former compatriots.',
        'shining star' : 'As the RENEGADE, you seek Redemption',
        'burn star' : 'brings justice to the worlds.',
        'edges' : ['Aristocrat', 'Assassin', 'Bureaucrat', 'Driver', 'Intelligence', 'Officer', 'Plutocrat', 'Trooper'],
    },
    'The Revolutionary': {
        'flavor text': 'You are the backbone of the Rebellion.\n         You\'re a soldier invested in the overthrow of the government.',
        'shining star': 'As the REVOLUTIONARY, you fight for CHANGE.',
        'burn star': 'changes the statis quo',
        'edges': ['Academic', 'Aristocrat', 'Commando', 'Firebrand', 'Mechanic', 'Organizer', 'Pilot', 'Spy'],
    },
    'The Robot': {
        'flavor text': 'According to the Killstar Republick, you are just a tool, a possession.\n         You have no rights. You are just a machine.',
        'shining star': 'As the ROBOT, you seek SELF',
        'burn star': 'is an expression of self',
        'edges': ['Assistant', 'Bucket', 'Fixer', 'Killer', 'Lifter', 'Megaputer', 'Spacer', 'Watchdog'],
    },
    'The Rogue': {
        'flavor text': 'You\'re not in this for the revolution - or that\'s what you tell people.\n         You are a free-wheeling, free-dealing individual that got caught up in the fight.',
        'shining star': 'As the ROGUE, you burn for FREEDOM',
        'burn star': 'frees someone',
        'edges': ['Crimer', 'Coyote', 'Duelist', 'Gambler', 'Coder', 'Racer', 'Thief', 'Smuggler'],
    },
    'The Ronin': {
        'flavor text': 'You are an outlaw warrior monk, a member of the fallen Amurai Warriors.\n         You are well trained in the use of LAZER SWORDS and mystical space magic.',
        'shining star': 'As the RONIN, you quest for PEACE.',
        'burn star': 'brings peace to a situation',
        'edges': ['Clairvoyant', 'Diplomat', 'General', 'Historian', 'Swordfighter', 'Teacher', 'Telekinetic', 'Telepath'],
    },
}

#---------------------------------------
## Generic Character Traits for Sci-Fi
#---------------------------------------
## first names
first_names = ['Kael', 'Zyra', 'Orin', 'Vexis', 'Taryn']

## last names
last_names = ['Draven', 'Quen', 'Vorr', 'Syndra', 'Kastix']

# standard genders and some taken from No Man's Sky
genders = ['male', 'female', 'non-binary', 'orthogonal', 'indeterminate', 'unknown']

crew_roles = [
    "Pilot", 
    "Engineer", 
    "Tactical Officer", 
    "Navigator", 
    "Medic", 
    "Science Officer", 
    "Xeno-Linguist", 
    "Security Chief", 
    "Mechanic", 
    "Smuggler"
]

recruitment_methods = [
    "Won in a cantina raffle.",
    "Found stowing away in the cargo hold.",
    "Joined after losing a bet.",
    "Accidentally teleported onto the ship.",
    "Saved from floating in deep space.",
    "Hired via an outdated space job listing.",
    "Turned up claiming 'destiny' sent them.",
    "Was already living in the ventilation system.",
    "Mistakenly delivered in a cargo shipment.",
    'Won in a cosmic claw machine',
    "Won bet with a smuggler who can\'t pay up",
    "Lost a bet with the ship's AI",
    'Absorbed from a sentient ooze',
    'Summoned by an ancient artifact',
    'Materialized from a teleporter accident',
    'Spawned from a quantum glitch',
    'Found in a space dumpster',
    'Delivered as a mail order henchman',
    'Rode in on a space whale',
    'A clone with no memory',
    'Found in a cryo-pod labeled "Do not open"',
    'Free bonus with a ship upgrade',
    'Was trapped in an ancient VR simulation',
    'As payment for a debt the AI forgot about',
    "Rehabilitated rogue AI that failed the Turing Test"
]

search_methods = [
    'Searching cloning facility clearance sale',
    'Analyzing unemployment database',
    'Posting an ad on space.craigslist.org',
    'Placing bid in intergalactic prison auction',
    "Parsing AI re-education camp 'graduates' ",
    "Cross-referencing expired cryo-prison logs",
    "Decrypting corporate employee termination logs",
    "Catfishing on Space Tinder",
    "Processing rejects from cybernetic augmentation trials",
    "Filtering Killstar Republick's Most Wanted List",
    'Scanning the lost-and-found bin at the spaceport',
    'Attempting bribe of bounty hunter for captured fugitives',
    "Surveilling cantina drunk tank",
    'Unfreezing random cryo-pod labeled "experimental"',
    'Tracking contestants eliminated from a death game show',
    "Collecting 'volunteers' from a forced corporate retreat",
    "Phishing Killstar Republick's executive email list",
    "Initiating trade with merchant for 'certified organic crew members'",
    "Processing debtors from AI bookmaking operation",
    'Extracting workers from an "unpaid internship" on mining asteroid',
    'Pressing random buttons on interdimensional recruitment kiosk',
    'Posting ad on "FindYourCrewmate.com" (not a scam, probably)',
    'Data-mining conspiracy theory forum',
]
###---------------------------
### SHIPS
###---------------------------

## Rebel Scum cannon lists
ship_sizes = {
    'Yacht' : 'd4',
    'Corvette' : 'd6', 
    'Frigate' : 'd8', 
    'Crusier' : 'd10'
}

ship_edges = [
    'Armor Plating', 
    'Bombs',
    'Cloaking Device', 
    'Starfighters', 
    'Runabout Shuttle', 
    'Jammers', 
    'Megaputer', 
    'Missiles', 
    'Passenger Amenities', 
    'Self Destruct', 
    'Super Thrusters'
]


## My own custom lists 
ship_names = [
    'Nebula\'s Edge',
    'Starfire Rapture',
    'Eclipse Voyager',
    'Iron Horizon',
    'Stellar Phoenix',
    'Celestial Fury',
    'Vortex Marauder',
    'Crimson Seraph',
    'Shadow\'s Embrace',
    'Obsidian Vanguard',
    'Galactic Reaver',
    'Titan\'s Wrath',
    'Voidstrider',
    'Astral Tempest',
    'Sunset Requiem',
    'Shadowstorm Cruiser',
    'Endeavor\'s Dawn',
    'Nova\'s Revenge',
    'Phantom Warden',
    'Cosmic Wraith'
]

ship_genders = [
    "Voidborn", 
    "Solarfluid", 
    "Quantumflux", 
    "Plasmatic",
    "Astrosexual", 
    "Unknowable", 
    "Nullgender", 
    "Mechafemme", 
    "Galactomale", 
    "Nebular", 
    "Hyperfluid", 
    "Anomaly", 
    "Singular", 
    "Interdimensional", 
    "Biocosmic", 
    "Spectral", 
    "Cryptoneutral", 
    "Timefluid",
    "Polymorphic"
]

ship_backstories = [
    "The Eternal Warranty. This ship was part of a failed manufacturer recall, but the warranty is still valid… somehow.",
    "The Ghost in the Drive. It once had an AI that refused to die. Now, it occasionally whispers cryptic messages.",
    "Refurbished from a Pirate Wreck. Rebuilt from the twisted hull of a legendary pirate's ship. Some say it still seeks revenge.",
    "Previously Owned by a Cult. The walls have strange carvings, and the autopilot sometimes tries to find an unknown 'holy planet.'",
    "The Government Blacklist Special. It was once part of a classified military experiment, but someone 'accidentally' sold it.",
    "Won in a Rigged Sabacc Game. Someone cheated to win this ship, and its previous owner still wants it back.",
    "Salvaged from a Battle Nobody Remembers. It was discovered in deep space, filled with old, unreadable logs and strange damage.",
    "A Relic of a Forgotten War. The markings belong to a nation that no longer exists. It's a flying history lesson… and a liability.",
    "Designed by a Mad Engineer. Nothing inside makes sense. Why is the hyperdrive in the bathroom?!",
    "The Ship That Shouldn't Fly. No one knows how it still works. Even the engineer just shrugs and walks away.",
    "Rescued from an Interdimensional Rift. It disappeared 100 years ago and reappeared last week—with a half-eaten sandwich on the console.",
    "Hacked Together from Junkyard Parts. Built by a desperate smuggler, it runs on luck and duct tape.",
    "The Party Barge. Once a luxury pleasure yacht, it was heavily modified by desperate mercenaries in a hurry.",
    "Once a Flying Prison. It used to be a high-security transport for dangerous criminals. The cells are still there… just in case.",
    "Registered to a Dead Person. Officially, the owner of this ship died 30 years ago. Legally speaking, you don't exist.",
    "Corporate Prototype Gone Wrong. A megacorp abandoned this 'cutting-edge' ship because of a 'minor' design flaw.",
    "The AI Won't Shut Up. The onboard AI is too advanced, and now it thinks it's a stand-up comedian.",
    "Salvaged from a Space Cult. The ship was abandoned near a dying star, and some say it carries a curse.",
    "Had a Previous Crew... Until It Didn't. The previous owners all disappeared under mysterious circumstances.",
    "Has a Mind of Its Own. The ship occasionally flies itself. It won't say why."
]

ship_extras = [
    "Laser Cannons", "Photon Shields", "Hyperdrive Engine",
    "Auto-Repair System", "Gravity Stabilizer", "Quantum AI Core",
    "Energy Deflectors", "Cargo Bay Expansion", "Advanced Sensors"
]

## funny add ons for ship construction loading screen
ship_traits = [
    "Turbocharged Ego Core", 
    "AI Personality Matrix", 
    "Infinite Cup Holder Capacity", 
    "Quantum Beard Generator", 
    "Mood-Based Hull Colors", 
    "Celestial Karaoke System", 
    "Gravitationally Confused Thrusters", 
    "Parallel Universe Detector",
    'Profanity Translation Matrix',
    'AI Sarcasm Subroutines'
]

building_words = ['Constructing', 'Creating', 'Erecting', 'Assembling', 'Developing', 'Forming', 'Fabricating', 'Establishing']
adjusting_words = ['Modifying', 'Altering', 'Tweaking', 'Calibrating', 'Fine-tuning', 'Swapping', 'Refining', 'Tailoring']
installing_words = ['Implementing', 'Mounting', 'Deploying', 'Integrating', 'Enabling', 'Configuring', 'Positioning']

ship_building_words = [building_words, adjusting_words, installing_words]

###---------------------------
### QUESTS
###---------------------------
adjectives = [
    'mysterious', 'grizzled', 'enigmatic', 'robotic', 'ancient', 'fierce', 'honorable',
    'stoic', 'galactic', 'alien', 'wounded', 'intelligent', 'charming', 'ruthless', 'shrewd'
]

npc_types = [
    'Bounty Hunter', 
    'Holo-Engineer', 
    'Smuggler', 
    'Rebel Spy', 
    'Space Pirate', 
    'Amurai Warrior',
    'Imperial Officer', 
    'Mercenary', 
    'Diplomat', 
    'Pilot', 
    'Warlord',
    'Scientist', 
    'Hacker', 
    'Droid', 
    'Merchant'
]

objectives = [
    'retrieve the lost artifact', 
    'infiltrate an enemy base', 
    'disable a space station defenses',
    'negotiate with an alien faction', 
    'repair a damaged ship', 
    'steal secret blueprints',
    'rescue a kidnapped senator', 
    'extract a valuable resource', 
    'deliver crucial data',
    'defend a convoy from pirates', 
    'capture a fugitive', 
    'decrypt an ancient text',
    'retrieve a prototype weapon', 
    'investigate a mysterious distress signal', 
    'escort a diplomat'
]

locations = [
    'an Abandoned Space Station',
    'an Alien Ruins',
    'an Asteroid Belt',
    'a Bio-Dome Colony',
    'a Black Hole Perimeter',
    'a Cryo-Lab Facility',
    'a Deep Space Relay',
    'a Deserted Moon Base',
    'a Dimensional Rift',
    'a Floating Megacity',
    'a Galactic Core',
    'a Hidden Rebel Outpost',
    'a Hyperdrive Repair Yard',
    'an Intergalactic Marketplace',
    'a Lost Planet',
    'a Nebula Research Station',
    'an Orbital Defense Platform',
    'a Quarantine Zone',
    'a Radiation Zone',
    'a Remote Mining Colony',
    'a Secret Military Bunker',
    'a Sentient AI Mainframe',
    'a Solar Observatory',
    'a Starship Graveyard',
    'a Subterranean Alien Hive',
    'a Terraforming Hub',
    'a Time Distortion Field',
    'an Underwater Research Lab',
    'a Warp Gate Nexus',
    'an Xeno-Biology Lab'
]

obstacles = [
    'a deadly asteroid field', 
    'an ambush by rival bounty hunters', 
    'a malfunctioning hyperdrive',
    'a treacherous pirate gang', 
    'an alien warlord', 
    'the Empire\'s heavy patrols', 
    'a dangerous nebula',
    'hostile wildlife', 
    'a malfunctioning droid', 
    'a deadly trap set by enemies', 
    'a collapsing space station',
    'a faction of rebels who oppose your mission', 
    'a fleet of Imperial Star Destroyers', 
    'a deadly bounty placed on your head', 
    'a deadly virus outbreak'
]

rewards = [
    'a large sum of credits', 
    'a rare starship upgrade', 
    'the location of a hidden planet',
    'an ancient relic of immense power', 
    'a valuable piece of technology', 
    'a fleet of loyal soldiers',
    'an exclusive contract', 
    'a dangerous weapon prototype', 
    'information about the galaxy\'s secrets',
    'a rare artifact with unknown abilities', 
    'access to a prestigious military rank', 
    'the promise of future alliances',
    'a mysterious alien ally', 
    'a powerful energy crystal', 
    'a high-ranking position in a faction'
]