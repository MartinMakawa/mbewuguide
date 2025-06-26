from typing import Dict, Any, Optional, List

# Consolidated crop knowledge base
def get_all_crops_knowledge_base() -> Dict[str, Dict[str, Any]]:
    return {
        "sunflower": sunflower_knowledge_base,
        "sugarcane": sugarcane_knowledge_base,
        "tobacco": tobacco_knowledge_base,
        "watermelon": watermelon_knowledge_base,
        "pumpkin": pumpkin_knowledge_base,
        "tomato": tomato_knowledge_base,
        "irish potato": irish_potato_knowledge_base,
        "beans": beans_knowledge_base,
        "onion": onion_knowledge_base,
        "cabbage": cabbage_knowledge_base,
        "cassava": cassava_knowledge_base,
        "rice": rice_knowledge_base,
        "maize": maize_knowledge_base,
    }

# --- Query Functions ---
def get_crop_knowledge(crop_name: str) -> Optional[Dict[str, Any]]:
    """Return the full knowledge base for a crop."""
    crops = get_all_crops_knowledge_base()
    return crops.get(crop_name.lower().strip())

def get_crop_section(crop_name: str, section: str) -> Optional[Any]:
    """Return a specific section (e.g., 'fertilizer_management') for a crop."""
    crop = get_crop_knowledge(crop_name)
    if crop:
        return crop.get(section)
    return None

# --- Step-by-Step Guidance ---
def get_crop_stages(crop_name: str) -> Optional[List[str]]:
    """Return the ordered list of growth stages for a crop, if available."""
    crop = get_crop_knowledge(crop_name)
    if not crop:
        return None
    # Try common keys for stages
    for key in ["growth_stages_and_management", "growth_stages", "growth_stages_and_care"]:
        if key in crop:
            stages = crop[key]
            if isinstance(stages, dict):
                return [v for k, v in sorted(stages.items(), key=lambda x: str(x[0]))]
            elif isinstance(stages, list):
                return stages
    return None

def get_next_stage(crop_name: str, current_stage_index: int) -> Optional[str]:
    """Return the next stage in the crop's lifecycle."""
    stages = get_crop_stages(crop_name)
    if stages and 0 <= current_stage_index < len(stages) - 1:
        return stages[current_stage_index + 1]
    return None

# --- Personalized Advice (Stub for future expansion) ---
def get_personalized_advice(crop_name: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
    """Return advice tailored to the user's data (farmer type, location, soil, etc.)."""
    crop = get_crop_knowledge(crop_name)
    if not crop:
        return {"error": "Crop not found in knowledge base."}
    # Example: tailor fertilizer advice based on farmer type
    advice = {}
    farmer_type = user_data.get("farmer_type")
    if farmer_type == "large_scale":
        advice["fertilizer_management"] = crop.get("fertilizer_management", "Use recommended rates and consider soil testing kits.")
    elif farmer_type == "small_scale":
        advice["fertilizer_management"] = crop.get("fertilizer_management", "Use organic manure and follow local extension advice.")
    else:
        advice["fertilizer_management"] = crop.get("fertilizer_management", "Follow general fertilizer guidelines.")
    # Add more personalization as needed
    return advice

# --- Example: General Crop Guidance (Short Summary) ---
def get_crop_guidance(crop_name: str) -> Any:
    crop = get_crop_knowledge(crop_name)
    if not crop:
        return {"error": "Crop not found in knowledge base."}
    profile = crop.get("crop_profile") or crop.get("crop_profile", {})
    summary = {
        "common_names": profile.get("common_names", []),
        "botanical_name": profile.get("botanical_name", ""),
        "growth_duration": profile.get("growth_duration", ""),
        "yield_range": profile.get("yield_range", ""),
        "economic_value": profile.get("economic_value", []),
    }
    return summary

# --- (Keep the original knowledge base dictionaries below) ---
sunflower_knowledge_base = {
    "crop_profile": {
        "common_names": ["Sunflower"],
        "botanical_name": "Helianthus annuus",
        "growth_duration": "70–150 days depending on variety",
        "yield_range": "1.5–3 tons/ha (oilseed) under good management",
        "economic_value": [
            "Major source of edible oil worldwide",
            "Used for snacks, birdseed, and ornamental purposes",
            "High demand in food and biofuel industries"
        ]
    },

    "climate_and_soil_requirements": {
        "temperature": "Optimal 20°C–25°C; tolerant to heat but sensitive to frost",
        "rainfall": "500–800 mm; drought tolerant but needs adequate moisture during flowering and seed filling",
        "soil_type": "Well-drained loamy or sandy soils with good fertility",
        "soil_pH": "6.0–7.5 (neutral to slightly acidic)",
        "altitude": "Up to 1,500 m above sea level"
    },

    "land_preparation": {
        "ploughing": "Deep ploughing (20–30 cm) to loosen soil",
        "leveling": "Well-leveled field to facilitate uniform planting and irrigation",
        "weed_removal": "Remove perennial weeds before planting",
        "fertility": "Incorporate well-decomposed organic manure or compost"
    },

    "variety_selection": {
        "criteria": [
            "High oil content (35-50%)",
            "Disease and pest resistance",
            "Short to medium duration based on local growing season",
            "Good seed size and weight"
        ],
        "popular_varieties": [
            "Sunrich, Mammoth, KBSH 1, PAC 36",
            "Local varieties recommended by agricultural research centers"
        ]
    },

    "seed_and_planting": {
        "seed_quality": "Certified, treated for seed-borne diseases",
        "seed_treatment": "Fungicide and insecticide treatment to prevent damping-off and seed pests",
        "planting_time": "At the onset of rains or with irrigation in dry areas",
        "planting_methods": [
            "Row planting preferred for better management",
            "Spacing: 60–75 cm between rows, 20–30 cm between plants",
            "Seed rate: 3–5 kg/ha depending on variety"
        ],
        "depth": "2.5–5 cm depending on soil moisture"
    },

    "fertilizer_management": {
        "basal_application": {
            "NPK": "60–90 kg N, 30–60 kg P2O5, 30–50 kg K2O per hectare",
            "split_application": [
                "Half nitrogen at planting",
                "Half nitrogen at early flowering stage"
            ]
        },
        "micronutrients": "Boron and zinc may be applied if deficient",
        "organic_matter": "Apply compost or farmyard manure at 5–10 tons/ha before planting"
    },

    "weed_management": {
        "critical_period": "First 30-40 days after planting",
        "methods": [
            "Manual weeding",
            "Mechanical cultivation between rows",
            "Pre- and post-emergence herbicides (e.g., Pendimethalin, Imazethapyr)"
        ],
        "mulching": "Useful in moisture conservation and weed suppression"
    },

    "irrigation_management": {
        "requirements": "Critical during flowering, seed development and filling stages",
        "methods": "Furrow, drip or sprinkler irrigation",
        "schedule": "Maintain soil moisture especially in dry spells; avoid waterlogging"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "sunflower moth": "Monitor traps and apply insecticides if threshold exceeded",
            "aphids": "Encourage natural predators or apply insecticides",
            "cutworms": "Soil treatment and timely planting",
            "seed weevils": "Seed treatment before planting"
        },
        "major_diseases": {
            "downy mildew": "Use resistant varieties and seed treatment",
            "rust": "Fungicides application and crop rotation",
            "powdery mildew": "Apply sulfur-based fungicides",
            "alternaria leaf spot": "Field sanitation and fungicide spray"
        },
        "IPM_strategies": [
            "Regular field scouting",
            "Use resistant varieties",
            "Crop rotation with non-host crops",
            "Balanced fertilization to avoid excess nitrogen"
        ]
    },

    "crop_management": {
        "thinning": "Remove weak plants to maintain recommended spacing",
        "staking": "Usually not required unless in windy areas",
        "pruning": "Not typically done",
        "disease monitoring": "Frequent scouting especially during humid conditions",
        "fertilizer top-ups": "Apply nitrogen at flowering stage for better seed development"
    },

    "harvesting": {
        "harvest_time": "When 75-85% of the seeds turn black/dark brown (physiological maturity)",
        "signs": [
            "Leaves yellow and dry",
            "Seeds hard and rattle inside the head"
        ],
        "harvesting_methods": [
            "Manual: cut heads and dry",
            "Mechanical harvesting: using combines where available"
        ],
        "post_harvest_handling": [
            "Dry seeds to 8-10% moisture content",
            "Clean to remove debris and immature seeds",
            "Store in cool, dry, pest-free conditions"
        ]
    },

    "post_harvest_processing_and_marketing": {
        "processing": [
            "Oil extraction by mechanical pressing or solvent extraction",
            "Seed cake used as animal feed"
        ],
        "value_addition": [
            "Cold-pressed sunflower oil for premium markets",
            "Sunflower snacks and confectionery",
            "Birdseed and ornamental uses"
        ],
        "market_channels": [
            "Local oil mills",
            "Food industry buyers",
            "Export markets"
        ],
        "quality_control": [
            "Seed oil content and purity",
            "Free fatty acid level",
            "Seed moisture content"
        ]
    },

    "smart_farming_practices": {
        "soil_testing": "Before planting to guide fertilizer application",
        "remote_sensing": "To detect crop stress and pest outbreaks",
        "precision_irrigation": "To optimize water use and improve yield",
        "mobile_apps": "For disease diagnosis and agronomic advice",
        "record_keeping": "Track inputs, planting dates, pest outbreaks, and yield"
    }
}
sugarcane_knowledge_base = {
    "crop_profile": {
        "common_names": ["Sugarcane"],
        "botanical_name": "Saccharum officinarum",
        "growth_duration": "10–24 months depending on variety and climate",
        "yield_range": "60–120 tons/ha of cane",
        "economic_value": [
            "Major source of sugar production globally",
            "Used in bioethanol, molasses, and rum industries",
            "High employment potential in rural areas",
            "Significant cash crop for farmers in tropical and subtropical regions"
        ]
    },

    "climate_and_soil_requirements": {
        "temperature": "Optimal 20°C–35°C; sensitive to frost",
        "rainfall": "1,200–1,500 mm/year with well-distributed rains",
        "soil_type": "Deep, well-drained loam or sandy loam",
        "soil_pH": "6.0–7.5 (neutral to slightly acidic)",
        "altitude": "Up to 1,200 m above sea level"
    },

    "land_preparation": {
        "ploughing": "Deep ploughing (30–40 cm) to break hardpan",
        "leveling": "Smooth field to facilitate irrigation and mechanized harvesting",
        "field_layout": "Prepare ridges or furrows depending on irrigation",
        "organic_matter": "Apply 20–30 tons/ha compost or farmyard manure before planting"
    },

    "variety_selection": {
        "criteria": [
            "High sugar content (brix %)",
            "Good ratooning ability",
            "Disease resistance (e.g., smut, rust)",
            "Adapted to local climate and soil"
        ],
        "popular_varieties": [
            "Co 86032, Co 8014 (India)",
            "N14, NCo310 (various tropical areas)",
            "Local recommended varieties based on agro-ecology"
        ]
    },

    "planting_material_and_methods": {
        "seed_cane": "Use healthy, disease-free stalks",
        "setts": {
            "size": "20–25 cm long with at least 2–3 buds",
            "treatment": "Fungicide dip to control sett rot"
        },
        "planting_methods": [
            "Trench planting: furrows 20–30 cm deep",
            "Flat planting: on well-prepared beds",
            "Spacing: 1.2–1.5 m between rows, 0.3–0.5 m between setts"
        ],
        "planting_time": "At start of rainy season or with irrigation availability"
    },

    "fertilizer_management": {
        "basal_application": {
            "NPK": "150–200 kg N, 60–90 kg P2O5, 90–120 kg K2O per hectare",
            "split_application": [
                "1/3 at planting",
                "1/3 at tillering (30–60 days)",
                "1/3 at grand growth phase (90–120 days)"
            ]
        },
        "micronutrients": "Zinc and boron recommended if deficient",
        "organic_fertilizer": "Top dress with compost or green manure crops"
    },

    "weed_management": {
        "early_weeding": "Manual or mechanical weeding within first 30 days",
        "herbicides": [
            "Pre-emergence: Atrazine or Diuron",
            "Post-emergence: Paraquat or Glyphosate (selective use)"
        ],
        "mulching": "Helps reduce weed pressure and conserve moisture"
    },

    "irrigation_management": {
        "requirement": "Water critical during germination, tillering, and grand growth",
        "methods": "Furrow, drip, or sprinkler irrigation",
        "schedule": "Maintain soil moisture without waterlogging; irrigate every 7–10 days in dry periods"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "stem borer": "Use pheromone traps, resistant varieties, and insecticides if needed",
            "white grubs": "Soil insecticides and crop rotation",
            "sugarcane aphids": "Natural predators and insecticides",
            "root borer": "Sanitation and insecticide soil treatments"
        },
        "major_diseases": {
            "red rot": "Plant resistant varieties, destroy infected stalks",
            "smut": "Use disease-free setts and resistant varieties",
            "leaf scald": "Remove infected leaves, apply fungicides",
            "ratoon stunting": "Use clean planting material"
        },
        "IPM_strategies": [
            "Regular field scouting",
            "Use of resistant varieties",
            "Crop rotation with non-host crops",
            "Sanitation and removal of infected material"
        ]
    },

    "crop_management": {
        "tillering_phase": "Encourage by timely fertilization and moisture management",
        "ratooning": "After first harvest, allow regrowth; manage weeds and fertilize for next cycle",
        "propping": "Support tall plants if needed to avoid lodging",
        "thinning": "Remove weak or damaged shoots"
    },

    "harvesting": {
        "harvest_time": "10–24 months after planting, depending on variety and climate",
        "maturity_signs": [
            "High brix % (14–18%)",
            "Leaves start yellowing",
            "Stalks become hard and dry at base"
        ],
        "harvest_method": [
            "Manual cutting with machete or mechanical harvester",
            "Cut stalks close to ground to maximize yield"
        ],
        "handling": "Avoid delays in processing to reduce sucrose loss"
    },

    "post_harvest_processing": {
        "transport": "Rapid transport to sugar mill to maintain sugar quality",
        "storage": "Minimal storage recommended; sugarcane degrades quickly",
        "by-products": [
            "Bagasse used as biofuel or paper pulp",
            "Molasses for animal feed or fermentation"
        ]
    },

    "value_addition_and_marketing": {
        "products": [
            "Raw sugar",
            "Refined sugar",
            "Ethanol/biofuel",
            "Molasses and jaggery"
        ],
        "market_channels": [
            "Sugar mills",
            "Cooperatives",
            "Local and export markets"
        ],
        "quality_control": [
            "Sugar content (brix) testing",
            "Purity and moisture content",
            "Timely harvesting and milling"
        ]
    },

    "smart_farming_practices": {
        "soil_testing": "Annual to adjust fertilizer rates",
        "remote_sensing": "Use drones or satellite imagery for crop monitoring",
        "precision_irrigation": "Sensors to optimize water use",
        "mobile_apps": "Pest and disease identification and advice",
        "record_keeping": "Track planting dates, inputs, and harvest data for continuous improvement"
    }
}
tobacco_knowledge_base = {
    "crop_profile": {
        "common_names": ["Tobacco"],
        "botanical_name": "Nicotiana tabacum",
        "growth_duration": "90–130 days depending on variety and type",
        "yield_range": "1,000–2,500 kg/ha cured leaf",
        "economic_value": [
            "Major cash crop with high export potential",
            "Used for cigarettes, cigars, chewing tobacco, and snuff",
            "Employment source for many rural farmers",
            "Requires strict quality control for marketability"
        ]
    },

    "climate_and_soil_requirements": {
        "temperature": "Ideal 20°C–30°C; sensitive to frost and extreme heat",
        "rainfall": "600–1,200 mm annually; well-distributed",
        "soil_type": "Light sandy loam to loam soils with good drainage",
        "soil_pH": "5.8–6.5 (slightly acidic to neutral)",
        "altitude": "Best grown between 800–1,600 m above sea level"
    },

    "land_preparation": {
        "ploughing": "Deep ploughing (30 cm) to loosen soil",
        "levelling": "Well-leveled seedbeds for nursery",
        "organic_matter": "Add 15–20 tons/ha well-decomposed manure or compost",
        "nursery_beds": "Prepare raised seedbeds with fine tilth"
    },

    "variety_selection": {
        "types": ["Virginia", "Burley", "Eastern Dark", "White Burley", "Oriental"],
        "criteria": "Choose according to climate, soil, and market demand",
        "resistance": "Select varieties with resistance to common diseases such as tobacco mosaic virus"
    },

    "nursery_management": {
        "seed_sowing": "Fine seeds sown thinly in prepared seedbeds or trays",
        "depth": "0.5 cm",
        "germination_period": "7–14 days",
        "seedling_care": [
            "Keep moist but avoid waterlogging",
            "Thin seedlings to avoid overcrowding",
            "Shade seedlings to protect from strong sun for first 2 weeks",
            "Apply light nitrogen fertilizer as foliar spray after 3 weeks"
        ],
        "seedling_age_for_transplant": "6–8 weeks when seedlings reach 15–20 cm tall"
    },

    "transplanting": {
        "timing": "Early morning or late afternoon to reduce transplant shock",
        "spacing": "75 cm between rows and 45 cm between plants (approx. 30,000–35,000 plants/ha)",
        "hole_preparation": "Dig holes or furrows to plant seedlings firmly",
        "water_after_transplant": "Water immediately to settle soil around roots"
    },

    "fertilizer_management": {
        "basal_application": {
            "NPK": "Apply 200–250 kg/ha (e.g., 100:50:50 kg N:P2O5:K2O) based on soil test",
            "split_application": [
                "1/3 at transplanting",
                "1/3 at early growth (3–4 weeks after transplanting)",
                "1/3 during topping (before flowering)"
            ]
        },
        "micronutrients": "Supplement with boron and magnesium if deficient",
        "organic_amendments": "Incorporate compost to improve soil fertility"
    },

    "weed_management": {
        "pre-emergence": "Use herbicides like pendimethalin if allowed",
        "manual_weeding": "Hand weed or hoe 2–3 times during early growth",
        "mulching": "Optional to conserve moisture and reduce weeds"
    },

    "irrigation_management": {
        "requirement": "Regular watering; avoid water stress especially at flowering and leaf expansion",
        "method": "Drip or furrow irrigation preferred",
        "schedule": "Irrigate when top 5 cm soil is dry, about once per week depending on weather"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "tobacco hornworm": "Manual removal or use Bacillus thuringiensis (Bt)",
            "aphids": "Insecticidal soap, neem oil",
            "whiteflies": "Yellow sticky traps, insecticides",
            "cutworms": "Soil tillage and insecticide seed treatment"
        },
        "major_diseases": {
            "tobacco mosaic virus (TMV)": "Use resistant varieties and sanitation",
            "black shank": "Crop rotation, fungicides like metalaxyl",
            "blue mold": "Fungicide sprays and resistant varieties",
            "root rot": "Avoid waterlogging and improve drainage"
        },
        "IPM_strategies": [
            "Crop rotation with non-host crops (e.g., maize)",
            "Field sanitation and removal of infected plants",
            "Use certified disease-free seedlings",
            "Pest monitoring and threshold-based insecticide use"
        ]
    },

    "crop_management": {
        "topping": "Remove the flower head at 6–8 weeks to promote leaf growth",
        "suckering": "Remove side shoots (suckers) weekly after topping",
        "staking": "Optional for some types to keep plants upright",
        "defoliation": "Hand or mechanical removal of lower leaves before harvest to improve curing"
    },

    "harvesting": {
        "harvest_time": "80–130 days after transplanting depending on variety",
        "maturity_signs": [
            "Leaves change color from dark green to yellowish-green",
            "Lower leaves start to wilt and become brittle",
            "Middle and upper leaves ready for harvest at different times"
        ],
        "harvest_method": [
            "Priming (picking leaves in batches from bottom to top)",
            "Cutting whole plants in one go (rare)"
        ],
        "harvesting_tools": "Sharp knives or sickles",
        "handling": "Handle leaves carefully to avoid bruising"
    },

    "post_harvest_processing": {
        "curing_methods": [
            "Air curing (for Burley): hang in well-ventilated barns for 4–8 weeks",
            "Flue curing (for Virginia): heat without smoke in curing barns for 5–7 days",
            "Sun curing (for Oriental): dried in sun, takes 10–20 days"
        ],
        "grading": "Sort leaves by color, size, and quality",
        "storage": "Store cured leaves in dry, cool, ventilated areas",
        "packaging": "Compress and bale for transport and sale"
    },

    "value_addition_and_marketing": {
        "products": [
            "Cured tobacco leaf",
            "Processed tobacco for cigarettes and cigars",
            "Chewing and snuff tobacco"
        ],
        "market_channels": [
            "Auction floors",
            "Contract farming agreements",
            "Direct sales to manufacturers"
        ],
        "quality_control": [
            "Moisture content between 12–15%",
            "Uniform color and texture",
            "Low contamination and foreign matter"
        ]
    },

    "smart_farming_practices": {
        "soil_testing": "Before planting for balanced fertilizer application",
        "weather_monitoring": "Avoid irrigation before rain to reduce disease risk",
        "mobile_apps": "Use apps for pest and disease identification",
        "record_keeping": "Track inputs, growth stages, and harvest dates for yield optimization"
    }
}
watermelon_knowledge_base = {
    "crop_profile": {
        "common_names": ["Watermelon"],
        "botanical_name": "Citrullus lanatus",
        "growth_duration": "80–100 days from planting to harvest",
        "yield_range": "20–50 tons/ha depending on variety and practices",
        "economic_value": [
            "High demand in fresh fruit markets",
            "Processed into juice, jam, and rind candy",
            "Export potential during dry season",
            "High water content (90–92%) – suitable for hot climates"
        ]
    },

    "climate_and_soil_requirements": {
        "temperature": "Optimal 24°C–30°C; sensitive to frost",
        "rainfall": "400–600 mm; requires dry conditions during fruiting",
        "soil_type": "Sandy loam, well-drained",
        "soil_pH": "6.0–7.5",
        "altitude": "Best below 1500 m above sea level"
    },

    "land_preparation": {
        "ploughing": "Deep ploughing followed by harrowing",
        "ridges/mounds": "Raised beds or mounds improve drainage",
        "organic_matter": "Apply 10–15 tons/ha of compost or manure"
    },

    "variety_selection": {
        "open_pollinated": ["Sugar Baby", "Charleston Gray"],
        "hybrids": ["Crimson Sweet", "F1 Zera", "F1 Sukari"],
        "selection_criteria": "Size, sweetness, disease resistance, rind color"
    },

    "planting": {
        "method": "Direct seeding or transplanting nursery seedlings",
        "spacing": "1.5–2.0 m between rows, 0.6–1.2 m between plants",
        "seed_rate": "2–4 kg/ha",
        "depth": "2–3 cm",
        "germination_period": "5–7 days"
    },

    "fertilizer_management": {
        "basal": "Apply DAP at 150–200 kg/ha at planting",
        "top_dressing": {
            "first": "CAN or urea at 50–100 kg/ha at vine initiation (2–3 weeks)",
            "second": "NPK (20:20:20) or potassium nitrate during fruiting"
        },
        "foliar_sprays": "Calcium and boron during flowering for fruit quality"
    },

    "weed_management": {
        "manual": "Early hand weeding or hoeing (first 3–4 weeks)",
        "mulching": "Black plastic or straw to suppress weeds and conserve moisture",
        "herbicides": "Pre-emergent options like alachlor or pendimethalin"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "aphids": "Spray with neem oil or insecticidal soap",
            "fruit flies": "Use traps and early harvesting",
            "melon worm": "Bacillus thuringiensis (Bt) or pyrethroid spray",
            "cutworms": "Soil drenching and field sanitation"
        },
        "major_diseases": {
            "fusarium wilt": "Use resistant varieties and crop rotation",
            "powdery mildew": "Sulfur-based fungicides or potassium bicarbonate",
            "downy mildew": "Copper fungicides or mancozeb sprays",
            "anthracnose": "Avoid overhead irrigation, use certified seed"
        },
        "IPM": [
            "Resistant varieties",
            "Field hygiene",
            "Crop rotation with cereals or legumes",
            "Drip irrigation to avoid wetting leaves"
        ]
    },

    "water_management": {
        "irrigation_need": "Moderate during growth, low during ripening",
        "critical_stages": ["Flowering", "Fruit set", "Fruit enlargement"],
        "method": "Drip irrigation recommended for efficiency and disease control",
        "excess_water_risk": "Can cause fruit splitting and poor sweetness"
    },

    "growth_stages_and_management": {
        "1": "Seedling (0–2 weeks): Watch for damping off",
        "2": "Vine growth (2–4 weeks): Apply top-dressing",
        "3": "Flowering (4–6 weeks): Pollination management",
        "4": "Fruit set and growth (6–10 weeks): Adequate water and nutrients",
        "5": "Maturity (10–14 weeks): Reduce watering for sweeter fruit"
    },

    "pollination_management": {
        "pollinators": "Bees are primary pollinators",
        "enhancement": "Encourage flowering plants nearby; avoid pesticides during bloom",
        "manual_pollination": "Can be done with a brush if bee activity is low"
    },

    "harvesting": {
        "maturity_signs": [
            "Dull hollow sound when tapped",
            "Tendril nearest fruit dries up",
            "Underside of fruit turns creamy yellow",
            "Surface color dulls"
        ],
        "harvest_method": "Cut with a sharp knife, leaving short stalk",
        "post_harvest_handling": {
            "sorting": "By size and ripeness",
            "grading": "Remove cracked or diseased fruits",
            "storage": "Cool, dry room; avoid direct sunlight",
            "transport": "Cushion fruits during transport to avoid bruising"
        }
    },

    "value_addition_and_marketing": {
        "products": [
            "Fresh slices",
            "Juice",
            "Fruit salad",
            "Rind pickles/candy",
            "Seeds (roasted or oil extraction)"
        ],
        "packaging": "Crates or mesh bags; label with harvest date and size grade",
        "market_targets": "Urban retailers, juice processors, supermarkets",
        "export_opportunity": "High in Gulf countries, Europe during hot seasons"
    },

    "smart_farming_practices": {
        "climate_smart": "Drip irrigation + mulching to conserve water",
        "mobile_tools": "Use weather apps to prevent fruit cracking from rains",
        "digital_tracking": "Monitor flowering and maturity dates",
        "contract_farming": "Reliable income via institutional buyers"
    }
}
pumpkin_knowledge_base = {
    "crop_profile": {
        "common_names": ["Pumpkin", "Winter Squash"],
        "botanical_name": "Cucurbita pepo / Cucurbita maxima",
        "growth_duration": "90–140 days depending on variety",
        "yield_range": "15–25 tons/ha (can exceed 30 tons/ha under good conditions)",
        "economic_value": [
            "Fruit (vegetable market and processing)",
            "Seeds (snack and oil extraction)",
            "Leaves (used as relish in many African dishes)",
            "Animal feed (from vines and excess produce)"
        ]
    },

    "climate_and_soil_requirements": {
        "temperature": "Optimal 22°C–32°C; frost-sensitive",
        "rainfall": "600–1,200 mm annually; needs moderate moisture",
        "soil_type": "Well-drained loam or sandy loam with organic matter",
        "soil_pH": "6.0–6.8",
        "special_notes": "Avoid poorly drained, compacted, or waterlogged soils"
    },

    "land_preparation": {
        "initial_ploughing": "20–30 cm depth to loosen soil",
        "harrowing": "To achieve a fine tilth",
        "ridges_or_mounds": "Common for moisture retention and root development",
        "organic_matter": "Apply 10–15 tons/ha compost or decomposed manure"
    },

    "variety_selection": {
        "popular_varieties": ["Waltham Butternut", "Sugar Pie", "Crown Prince", "Kurokawa"],
        "selection_criteria": "Market preference, shelf life, disease resistance, flesh quality"
    },

    "planting": {
        "season": "After onset of rains or under irrigation",
        "spacing": {
            "mounds": "1.5–2.5 m between rows and plants",
            "flatbeds": "2 m x 1.5 m in fertile soils"
        },
        "seed_rate": "3–5 kg/ha",
        "depth": "2–4 cm deep",
        "germination_time": "5–10 days depending on temperature"
    },

    "fertilizer_management": {
        "basal": "Apply NPK 20:10:10 at 200–300 kg/ha at planting",
        "top_dressing": "Urea at 100 kg/ha 3–4 weeks after emergence",
        "organic_boost": "Frequent compost tea or diluted manure application",
        "trace_elements": "Add boron and zinc if soil tests indicate deficiency"
    },

    "weed_management": {
        "manual_weeding": "During early stages; vines suppress weeds later",
        "mulching": "Straw, grass or plastic mulch reduces weeds and preserves moisture",
        "herbicides": "Use pre-emergence herbicides like alachlor if needed"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "squash bugs": "Control with neem spray or pyrethroids",
            "aphids": "Spray imidacloprid; monitor with yellow sticky traps",
            "fruit flies": "Bait traps and bag fruits if needed",
            "cutworms": "Apply soil insecticides early"
        },
        "major_diseases": {
            "powdery mildew": "Use sulfur-based fungicides",
            "downy mildew": "Use mancozeb or copper-based fungicides",
            "anthracnose": "Practice crop rotation and clean seed use",
            "mosaic virus": "Control aphid vectors, remove infected plants"
        },
        "IPM": [
            "Crop rotation with cereals or legumes",
            "Sanitize tools and avoid over-irrigation",
            "Resistant varieties",
            "Proper field spacing"
        ]
    },

    "water_management": {
        "frequency": "Weekly irrigation during dry spells",
        "critical_stages": [
            "Flowering",
            "Fruit setting",
            "Fruit bulking"
        ],
        "methods": "Drip or furrow irrigation preferred; avoid waterlogging"
    },

    "growth_stages_and_management": {
        "1": "Germination (0–10 days)",
        "2": "Vine development (10–30 days): Weed and fertilize",
        "3": "Flowering (30–50 days): Ensure moisture and pollinator access",
        "4": "Fruit set and bulking (50–100+ days): Pest control and irrigation",
        "5": "Maturity and ripening (100–140 days)"
    },

    "harvesting": {
        "time": "When skin hardens and stem dries out",
        "method": "Cut with part of the stalk; avoid bruising",
        "post_harvest": {
            "curing": "Store in sun for 7–10 days to toughen skin",
            "storage": "Cool, dry area (can last 3–6 months)",
            "grading": "By size, ripeness, and external damage"
        }
    },

    "value_addition_and_marketing": {
        "products": [
            "Pumpkin puree",
            "Pumpkin flour",
            "Pumpkin seed oil",
            "Dried leaves",
            "Baby food and animal feed"
        ],
        "processing_tips": "Dry and grind seeds for flour; cook and pack puree for resale",
        "markets": "Hotels, urban groceries, processing plants",
        "export_tip": "Organic or heirloom varieties attract higher prices"
    },

    "smart_farming_practices": {
        "soil_testing": "Mandatory before heavy fertilizer use",
        "bee_integration": "Improve pollination and yield via beekeeping",
        "mobile_advice": "Apps for pest ID and market access",
        "recordkeeping": "Track planting dates, costs, yield for optimization"
    }
}
tomato_knowledge_base = {
    "crop_profile": {
        "common_names": ["Tomato"],
        "botanical_name": "Solanum lycopersicum",
        "growth_duration": "75–90 days (determinate); up to 120 days (indeterminate)",
        "yield_range": "25–40 tons/ha (can exceed 60 tons/ha with optimal management)",
        "economic_value": ["Fresh market", "Processing (paste, sauce)", "Export crop", "Kitchen gardening"]
    },

    "climate_and_soil_requirements": {
        "temperature": "18°C–28°C optimal",
        "sensitive_to": ["Frost", "Extreme heat (>35°C)", "High humidity"],
        "rainfall": "600–1200 mm; avoid heavy rains during flowering/fruiting",
        "soil_type": "Well-drained loam or sandy loam, rich in organic matter",
        "soil_pH": "6.0–6.8"
    },

    "land_preparation": {
        "clearing": "Remove weeds and debris",
        "tillage": "Plough to 20–30 cm; harrow to a fine tilth",
        "raised_beds": "Encouraged in heavy soils or rainy seasons",
        "basal_manure": "Add 10–20 tons/ha well-decomposed compost or manure"
    },

    "variety_selection": {
        "fresh_market": ["Rio Grande", "Money Maker", "Marglobe", "Tengeru 97"],
        "processing": ["Roma VF", "Cal J", "UC82"],
        "climate_resilient": ["Anna F1", "Kilele F1 (heat-tolerant)"],
        "criteria": "Yield potential, disease resistance, shelf-life, fruit firmness"
    },

    "nursery_management": {
        "duration": "21–30 days before transplanting",
        "seed_rate": "150–250 g/ha",
        "seedbed_size": "1 m x 5 m, raised",
        "sowing_depth": "1–1.5 cm",
        "care": "Watering, shading, and hardening-off before transplanting",
        "transplanting_stage": "When 4–5 true leaves are formed"
    },

    "planting": {
        "spacing": {
            "determinate": "60 cm x 45 cm",
            "indeterminate": "100 cm x 60 cm"
        },
        "planting_depth": "Transplant up to first true leaves",
        "time": "Onset of rains or under irrigation",
        "staking": "Required for indeterminate varieties"
    },

    "fertilizer_management": {
        "basal": "Apply DAP or NPK 17:17:17 at 200–300 kg/ha at planting",
        "top_dressing": [
            {"time": "3–4 weeks after transplanting", "fertilizer": "CAN or urea at 100–150 kg/ha"},
            {"time": "At flowering", "fertilizer": "NPK 15:15:15 or foliar feeds rich in potassium"}
        ],
        "organic_option": "Use compost tea or fermented manure regularly"
    },

    "irrigation": {
        "method": "Drip or furrow irrigation preferred",
        "frequency": "Every 3–5 days depending on soil and stage",
        "critical_stages": ["Flowering", "Fruit setting", "Fruit enlargement"],
        "avoid": "Waterlogging and overhead irrigation during flowering"
    },

    "weed_management": {
        "manual": "Weed before transplanting and 2–3 times after",
        "mulching": "Suppresses weeds and retains moisture",
        "herbicide_option": "Paraquat or Glyphosate before planting"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "tomato fruit worm": "Spray Spinosad or Bt-based products",
            "whiteflies": "Use neem oil, imidacloprid",
            "thrips and aphids": "Insecticidal soaps or pyrethroids"
        },
        "major_diseases": {
            "early blight": "Mancozeb or copper-based fungicides weekly",
            "late blight": "Metalaxyl or chlorothalonil during wet weather",
            "bacterial wilt": "Use resistant varieties; rotate with maize",
            "powdery mildew": "Sulfur-based fungicides or baking soda spray"
        },
        "IPM_tips": [
            "Crop rotation",
            "Planting trap crops like marigold",
            "Using yellow sticky traps",
            "Field sanitation"
        ]
    },

    "growth_stages_and_management": {
        "1": "Nursery (0–30 days): Keep shaded, watered",
        "2": "Transplanting (30–40 days): Harden seedlings",
        "3": "Vegetative (40–60 days): Weed and apply fertilizers",
        "4": "Flowering (60–75 days): Moisture critical; start staking",
        "5": "Fruiting (75–100 days): Fertilize and monitor pests",
        "6": "Ripening (100–120 days): Reduce watering; harvest ripe fruits"
    },

    "harvesting": {
        "start": "75–90 days after transplanting depending on variety",
        "method": "Harvest by hand at mature-green to red-ripe stage",
        "frequency": "Every 2–3 days during peak season",
        "postharvest": {
            "sorting": "Remove cracked, bruised, or diseased fruits",
            "cleaning": "Dry wiping preferred; avoid wetting",
            "storage": "Cool, dry area; use crates to prevent bruising",
            "temperature": "12–16°C with 85–90% RH"
        }
    },

    "marketing_and_value_addition": {
        "products": ["Tomato paste", "Sauce", "Sun-dried tomatoes"],
        "direct_sales": "Markets, restaurants, schools",
        "cooperative_model": "For contract farming or bulk selling",
        "packaging": "Use plastic crates or boxes for transport"
    },

    "smart_farming_practices": {
        "tech": ["Soil sensors", "Tomato disease identification apps"],
        "data_logging": "Log watering, pest issues, harvest volume",
        "weather_monitoring": "Avoid rainy transplanting days or disease outbreaks",
        "mobile_advice": "Use farmer apps for localized alerts"
    }
}
irish_potato_knowledge_base = {
    "crop_profile": {
        "common_names": ["Irish Potato", "White Potato"],
        "botanical_name": "Solanum tuberosum",
        "growth_duration": "90–130 days depending on variety",
        "yield_range": "15–30 tons/ha (can reach 40 tons/ha under optimal management)",
        "economic_value": ["Food crop", "Chips and crisps industry", "Animal feed", "Export market"]
    },

    "climate_and_soil_requirements": {
        "altitude_range": "1500–3000 meters above sea level",
        "temperature": "15°C–20°C optimal",
        "rainfall": "750–1200 mm, well distributed",
        "soil_type": "Well-drained, fertile sandy loam or loam",
        "soil_pH": "5.5–6.5",
        "sensitivity": "Waterlogging, extreme heat or frost"
    },

    "land_preparation": {
        "clearing": "Remove weeds and prior crop residues",
        "ploughing": "Deep tillage to loosen soil (20–30 cm depth)",
        "ridging": "Create ridges 60–75 cm apart for tuber expansion",
        "organic_matter": "Add 10–15 tons/ha of compost or decomposed manure"
    },

    "variety_selection": {
        "early_maturing": ["Shangi", "Tigoni"],
        "high_yielding": ["Kenya Mpya", "Sherekea"],
        "processing_varieties": ["Markies", "Dutch Robjin"],
        "criteria": "Based on altitude, rainfall, market preference, disease resistance"
    },

    "planting": {
        "seed_type": "Certified disease-free seed tubers (cut or whole)",
        "cutting_seeds": "Cut large tubers into 40–60 g pieces with at least 2 eyes each",
        "spacing": {
            "rows": "75 cm apart",
            "within_row": "30 cm"
        },
        "planting_depth": "10–15 cm",
        "time": "At onset of rains or with adequate irrigation",
        "seed_rate": "2.5–3 tons/ha (whole tubers); 1.5–2 tons/ha (cut tubers)"
    },

    "fertilizer_management": {
        "basal": "Apply NPK (17:17:17) or DAP at 200–300 kg/ha",
        "top_dressing": "Apply CAN or Urea at 150–200 kg/ha after 30–40 days",
        "split_application": "Split top dressing to avoid leaching losses",
        "organic_alternatives": "Farmyard manure + bone meal or rock phosphate"
    },

    "irrigation": {
        "critical_stages": ["Tuber initiation", "Tuber bulking"],
        "frequency": "Every 7–10 days depending on soil type",
        "method": "Furrow or drip irrigation; avoid overhead during flowering",
        "note": "Ensure uniform moisture to avoid tuber cracking"
    },

    "weed_management": {
        "manual": "Weed 2–3 times before canopy closes",
        "mulching": "Suppress weeds and maintain soil moisture",
        "herbicides": {
            "pre_emergence": "Use Metribuzin or Pendimethalin cautiously",
            "post_emergence": "Use selective herbicides if needed"
        }
    },

    "pest_and_disease_control": {
        "major_pests": {
            "potato tuber moth": "Bury tubers; spray with Lambda-cyhalothrin",
            "aphids": "Spray with systemic insecticides or neem oil",
            "cutworms": "Baiting and soil insecticides during land prep"
        },
        "major_diseases": {
            "late blight": "Weekly spray with Mancozeb or Metalaxyl-based fungicides",
            "early blight": "Use preventive copper-based fungicides",
            "bacterial wilt": "Use clean seed and rotate with non-solanaceous crops",
            "black scurf": "Use treated seed and maintain clean fields"
        },
        "IPM_tips": [
            "Rotate with legumes or cereals",
            "Plant certified seeds",
            "Field sanitation and early blight scouting"
        ]
    },

    "growth_stages_and_management": {
        "1": "Sprouting (0–20 days): Ensure moist soil",
        "2": "Vegetative (20–40 days): Weed, apply first top dress",
        "3": "Tuber initiation (40–60 days): Apply second fertilizer; irrigate well",
        "4": "Tuber bulking (60–90 days): Consistent moisture; watch for pests",
        "5": "Maturation (90–130 days): Reduce watering; prepare for harvest"
    },

    "harvesting": {
        "timing": "When 50–60% foliage is yellow and dry; 2–3 weeks after haulm destruction",
        "method": "Use digging fork or plough; avoid bruising tubers",
        "curing": "Cure tubers for 10–14 days in shade to harden skin",
        "harvest_yield": "15–30 tons/ha (higher under intensive farming)"
    },

    "post_harvest_handling": {
        "cleaning": "Remove excess soil gently; no washing",
        "grading": "By size, shape, and absence of rot/damage",
        "storage": {
            "structure": "Ventilated cool rooms or diffused light stores",
            "temperature": "4–10°C for table potatoes; 12–15°C for seed potatoes",
            "humidity": "85–95%",
            "sprouting_prevention": "Use sprout inhibitors or store in the dark"
        }
    },

    "marketing_and_value_addition": {
        "products": ["Chips", "Crisps", "Mashed potatoes", "Starch"],
        "processing_units": "Sell to processors or cooperatives",
        "grade_standards": "Size, cleanliness, skin color, no damage",
        "value_addition": [
            "Frozen chips",
            "Potato flour",
            "Starch extraction"
        ]
    },

    "smart_farming_practices": {
        "digital_tools": ["Potato farming apps", "Remote moisture sensors"],
        "record_keeping": ["Input use, rainfall, disease outbreak, yields"],
        "soil_testing": "Essential for nutrient planning and pH adjustment"
    }
}
beans_knowledge_base = {
    "crop_profile": {
        "common_names": ["Beans", "Common beans", "Dry beans", "Green beans"],
        "botanical_name": "Phaseolus vulgaris",
        "varieties": ["Navy", "Kidney", "Pinto", "Black", "Mottled", "Green snap beans"],
        "uses": ["Dry grain", "Green pods", "Forage", "Soil fertility via nitrogen fixation"],
        "growth_duration": "60–120 days depending on variety",
        "average_yield": "1.0–2.5 tons/ha (can go up to 3.5 with irrigation and improved practices)"
    },

    "climate_and_soil_requirements": {
        "altitude_range": "500–2000 m above sea level",
        "temperature": "18°C–28°C optimal",
        "rainfall": "300–500 mm during growing season (well-distributed)",
        "soil_type": "Fertile, well-drained loam or sandy loam",
        "soil_pH": "6.0–6.8 preferred",
        "sensitivity": "Waterlogging, acidic soils, salinity"
    },

    "land_preparation": {
        "clearing": "Remove bushes, crop residues, and weeds",
        "tillage": "Plough and harrow to fine tilth",
        "ridges_or_flats": "Plant on flat land or raised beds depending on drainage",
        "organic_matter": "Apply 5–10 tons/ha of decomposed manure or compost before planting"
    },

    "variety_selection": {
        "early_maturing": ["K132", "CAL 96"],
        "disease_resistant": ["NABE 14", "SEF 06007"],
        "climbing_types": ["MAC 13", "G2333"]  # higher yields but require staking

    },

    "planting": {
        "seed_rate": "60–75 kg/ha for bush beans, 30–40 kg/ha for climbers",
        "spacing": {
            "bush": "40–50 cm between rows, 10–15 cm within row",
            "climbing": "75–90 cm between rows, 20–30 cm within row"
        },
        "depth": "2.5–5 cm depending on soil moisture",
        "seed_treatment": "Use fungicide + rhizobium inoculation for nodulation",
        "planting_time": "At onset of rains for rainfed; year-round for irrigated"
    },

    "fertilizer_and_soil_fertility": {
        "starter_fertilizer": {
            "DAP": "Apply 100–150 kg/ha at planting",
            "or_compost": "10 tons/ha for organic systems"
        },
        "top_dressing": {
            "Urea": "Apply 50–70 kg/ha at early flowering (only if needed)",
            "CAN": "Alternative to Urea, improves pod fill"
        },
        "liming": "Apply lime to correct acidity (if pH < 5.5)"
    },

    "irrigation": {
        "critical_stages": ["Germination", "Flowering", "Pod filling"],
        "frequency": "Every 5–7 days during dry spells",
        "method": "Drip or furrow irrigation to avoid leaf wetting",
        "avoid": "Irrigation during pod drying — causes fungal rot"
    },

    "weed_management": {
        "manual_weeding": "2–3 times per season (15, 30, and 45 days after planting)",
        "mulching": "Retains moisture and suppresses weeds",
        "herbicides": {
            "pre_emergence": "Pendimethalin",
            "post_emergence": "Use with caution; beans are sensitive"
        }
    },

    "pest_and_disease_control": {
        "major_pests": {
            "aphids": "Spray neem extract or systemic insecticides like Dimethoate",
            "bean fly": "Plant early, apply systemic insecticide at seedling stage",
            "cutworms": "Baiting and field sanitation",
            "pod borers": "Use insecticide at early podding stage"
        },
        "major_diseases": {
            "angular_leaf_spot": "Use resistant varieties and Mancozeb sprays",
            "rust": "Fungicide spray at early sign, avoid overhead irrigation",
            "root rot": "Avoid overwatering, use crop rotation",
            "anthracnose": "Certified seed, copper fungicides"
        },
        "IPM_tips": [
            "Use certified disease-free seeds",
            "Field hygiene: Remove infected plants",
            "Rotate with maize, sorghum, or other non-legumes"
        ]
    },

    "growth_stages_and_management": {
        "1": "Germination (0–10 days): Maintain moisture",
        "2": "Vegetative (10–30 days): Weeding and top-dressing",
        "3": "Flowering (30–50 days): Avoid water stress",
        "4": "Pod development (50–70 days): Key yield stage",
        "5": "Maturity (70–100+ days): Stop watering to dry pods"
    },

    "harvesting": {
        "dry_beans": {
            "harvest_time": "When 80–90% of pods turn brown and rattle when shaken",
            "method": "Hand-pick or cut entire plants; thresh and dry",
            "post_harvest": "Dry beans to 12–13% moisture before storage"
        },
        "green_beans": {
            "harvest_time": "60–75 days after sowing",
            "method": "Pick tender pods every 3–4 days",
            "storage": "Cool, humid conditions to preserve freshness"
        }
    },

    "post_harvest_management": {
        "threshing": "Use tarpaulin to avoid contamination",
        "drying": "Sun dry to 12–13% moisture",
        "storage": {
            "bags": "Use airtight bags (PICS or Super Grain bags)",
            "pest_control": "Use dried neem leaves or fumigation if needed",
            "duration": "Can store for 6–12 months if well dried and protected"
        }
    },

    "marketing_and_economics": {
        "market_channels": ["Local markets", "Export", "Food processors"],
        "grading": "Clean and sort by size and color",
        "value_addition": ["Packaging in small consumer packs", "Canned beans"],
        "profit_tips": [
            "Target off-season harvest",
            "Join farmer groups for bulk selling",
            "Sell shelled and graded beans"
        ]
    },

    "smart_farming_tips": {
        "record_keeping": ["Dates, inputs, varieties, yield"],
        "digital_tools": ["Farming apps, mobile weather updates"],
        "soil_testing": "Use mobile labs or nearby extension services before planting"
    }
}
onion_knowledge_base = {
    "crop_profile": {
        "botanical_name": "Allium cepa",
        "family": "Amaryllidaceae",
        "types": ["Red onion", "White onion", "Yellow onion", "Shallots"],
        "maturity_days": "90–150 days depending on variety and climate",
        "yield_potential": "20–40 tons/ha under good management",
        "uses": ["Cooking", "Processing (powder, paste)", "Medicinal", "Dehydration industry"]
    },

    "climate_and_soil": {
        "temperature_range": "12°C–24°C during growth; 30°C+ for bulb formation",
        "rainfall_needs": "500–700 mm well-distributed; too much rain causes rot",
        "altitude_range": "300–1800 m above sea level",
        "soil_type": "Well-drained sandy loam or loam",
        "soil_pH": "6.0–6.8 optimal",
        "sensitivity": "Waterlogging, acidic soil, salinity"
    },

    "land_preparation": {
        "clearing": "Remove weeds and residues",
        "tillage": "Plough 20–30 cm deep; fine tilth for bulb formation",
        "bed_preparation": "Raised beds or flat beds; avoid water accumulation",
        "organic_matter": "Add 15–20 tons/ha of compost or decomposed manure"
    },

    "nursery_and_transplanting": {
        "seed_rate": "4–6 kg/ha",
        "nursery_duration": "6–8 weeks",
        "sowing_method": "Line sowing 1 cm deep; 10 cm between rows",
        "transplanting_age": "45–60 days old seedlings",
        "spacing": "15 x 10 cm or 20 x 10 cm depending on variety",
        "hardening": "Reduce watering 7 days before transplanting"
    },

    "direct_seeding_option": {
        "method": "Use seed drills or by hand",
        "spacing": "Line sowing at 20–30 cm between rows and 10 cm within row",
        "advantage": "Saves time and nursery cost",
        "limitation": "Weed competition early on"
    },

    "fertilizer_management": {
        "basal_fertilizer": {
            "DAP": "Apply 200–250 kg/ha at planting",
            "manure": "Well-rotted manure 15–20 tons/ha during land prep"
        },
        "top_dressing": {
            "Urea": "Apply 100–120 kg/ha in 2 splits at 3 and 6 weeks after transplanting",
            "CAN": "Optional in place of Urea"
        },
        "micronutrients": {
            "Sulphur": "Essential for bulb quality and pungency",
            "Zinc and Boron": "Spray if deficiency symptoms appear"
        }
    },

    "irrigation_management": {
        "method": "Furrow irrigation, drip preferred for water efficiency",
        "frequency": "Every 5–7 days initially, then 10–14 days during bulb formation",
        "avoid": "Water stress at bulb formation and excess moisture near harvest"
    },

    "weed_management": {
        "manual_weeding": "At 3 and 6 weeks after transplanting",
        "mulching": "Suppress weeds and conserve soil moisture",
        "herbicides": "Use pre-emergence herbicides like Pendimethalin if needed"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "onion thrips": "Spray with spinosad or neem-based products",
            "cutworms": "Bait with poison bran or apply Chlorpyrifos in soil",
            "leaf miners": "Use yellow sticky traps and systemic insecticides"
        },
        "major_diseases": {
            "purple blotch": "Use Mancozeb or copper oxychloride sprays",
            "downy mildew": "Spray with Metalaxyl or Ridomil Gold",
            "neck rot": "Avoid overhead irrigation, proper drying post-harvest",
            "fusarium basal rot": "Crop rotation and well-drained soil"
        }
    },

    "growth_stages_and_care": {
        "1": "Germination (0–10 days): Regular watering and shading",
        "2": "Seedling stage (10–45 days): Weeding and nursery maintenance",
        "3": "Transplanting (45–60 days)",
        "4": "Vegetative growth (2–6 weeks post-transplant): Nitrogen boost",
        "5": "Bulb initiation and swelling (6–12 weeks): Maximize water and nutrients",
        "6": "Bulb maturation (12–16 weeks): Reduce watering to prevent splitting"
    },

    "harvesting": {
        "indicators": "Top leaves bend over and dry naturally",
        "harvest_time": "90–120 days from transplanting",
        "method": "Lift bulbs carefully; avoid bruising",
        "curing": "Dry in field for 7–14 days until necks are fully dry",
        "expected_yield": "20–40 tons/ha under optimal conditions"
    },

    "post_harvest_handling": {
        "cleaning": "Remove loose soil and dry outer scales",
        "grading": "Sort by size and remove damaged bulbs",
        "storage": {
            "conditions": "Cool, dry, well-ventilated area",
            "methods": "Net bags, well-ventilated crates",
            "storage_duration": "Up to 4–6 months at 0°C–5°C with low humidity"
        },
        "transport": "Avoid high stacks; proper aeration needed"
    },

    "marketing_and_economics": {
        "high_value_markets": ["Supermarkets", "Export markets", "Processors"],
        "value_addition": ["Onion powder", "Onion paste", "Dehydrated flakes"],
        "price_stabilization": "Stagger planting to avoid seasonal price drops",
        "input_costs": "Ranges $1,000–$1,800 per ha depending on variety and intensity"
    },

    "common_problems_and_solutions": {
        "splitting_bulbs": "Caused by late heavy irrigation or excess nitrogen",
        "rotting": "Avoid wet soils and ensure proper curing before storage",
        "small_bulbs": "Caused by overcrowding or nutrient deficiency"
    },

    "smart_farming_tips": {
        "technologies": [
            "Drip irrigation to save water",
            "Solar dryers for curing",
            "Mobile apps for market pricing (e.g., Esoko, AgriEdge)"
        ],
        "record_keeping": [
            "Seed variety and planting date",
            "Fertilizer and chemical application records",
            "Yield and price per kg"
        ]
    }
}
cabbage_knowledge_base = {
    "crop_profile": {
        "botanical_name": "Brassica oleracea var. capitata",
        "family": "Brassicaceae (Cruciferae)",
        "types": ["Green cabbage", "Red cabbage", "Savoy cabbage"],
        "maturity_days": "70–120 days depending on variety",
        "yield_potential": "25–60 tons/ha under good management",
        "uses": ["Cooking vegetable", "Salads", "Processing (sauerkraut, kimchi)"],
    },

    "climate_and_soil": {
        "temperature_range": "15°C–20°C optimal, tolerates down to 10°C",
        "rainfall_needs": "400–800 mm well-distributed; supplement with irrigation",
        "altitude_range": "600–2800 m above sea level",
        "soil_type": "Deep, well-drained fertile loam or sandy loam",
        "soil_pH": "6.0–6.8 (slightly acidic to neutral)",
        "sensitivity": "Does not tolerate waterlogging; sensitive to acidic soils (risk of clubroot)"
    },

    "land_preparation": {
        "clearing": "Remove weeds and crop residues",
        "tillage": "Deep ploughing (30 cm), followed by harrowing",
        "bed_preparation": "Raised beds or ridges to prevent waterlogging",
        "fertility_boost": "Apply decomposed manure or compost (10–15 tons/ha)"
    },

    "seedling_nursery": {
        "nursery_bed_size": "1 m wide, length as needed",
        "sowing_depth": "1–2 cm deep",
        "spacing_in_nursery": "1 cm apart in rows",
        "care": {
            "watering": "Daily light irrigation",
            "shading": "Provide partial shade using grass or netting",
            "hardening": "Reduce watering and shade 7 days before transplanting",
        },
        "transplanting_age": "4–6 weeks old, 4–6 true leaves",
        "seed_rate": "350–500 g/ha depending on spacing"
    },

    "field_transplanting": {
        "spacing": "60 x 60 cm or 75 x 45 cm depending on variety",
        "watering": "Water nursery and transplant hole before and after planting",
        "best_time": "Cloudy day or late afternoon to avoid transplant shock"
    },

    "fertilizer_management": {
        "organic": "10–15 tons/ha well-decomposed manure during land prep",
        "basal": {
            "NPK": "Use NPK 17:17:17 or 20:10:10 at 200–400 kg/ha"
        },
        "top_dressing": {
            "Urea": "Apply 100–150 kg/ha in 2 splits (3 weeks and 6 weeks after transplant)",
            "CAN": "Can be used as an alternative to Urea for nitrogen source"
        },
        "micronutrients": "Use boron and molybdenum if deficiency signs show (e.g., hollow stem)"
    },

    "irrigation_and_water": {
        "method": "Drip or furrow recommended",
        "frequency": "2–3 times per week depending on rainfall and growth stage",
        "avoid": "Water stress during head formation; avoid overwatering (causes root rot)"
    },

    "weed_management": {
        "manual_weeding": "At 2 and 5 weeks after transplanting",
        "mulching": "Use straw or plastic mulch to conserve moisture and suppress weeds",
        "herbicide_use": "Pre-emergence herbicides may be used cautiously under expert advice"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "diamondback_moth": "Spray with Bt (Bacillus thuringiensis), neem extract, or spinosad",
            "aphids": "Use insecticidal soap or Imidacloprid",
            "cabbage looper": "Monitor and use pheromone traps or Bt-based pesticides",
            "cutworms": "Baiting with poisoned bran or soil drenching with Chlorpyrifos"
        },
        "major_diseases": {
            "black rot": "Use resistant varieties, copper-based fungicides, and crop rotation",
            "clubroot": "Avoid acidic soils (lime if needed), improve drainage",
            "downy mildew": "Ensure spacing and spray with Mancozeb or Metalaxyl",
            "alternaria leaf spot": "Use certified seed and rotate crops",
        }
    },

    "growth_stages_and_care": {
        "1": "Transplanting (0–1 week): Establishment phase",
        "2": "Vegetative growth (2–5 weeks): Leaf and stem expansion",
        "3": "Head initiation (6–8 weeks): Start top dressing and intense monitoring",
        "4": "Head development (8–12 weeks): Ensure sufficient water and pest control",
        "5": "Maturity (12–16 weeks): Tight heads, ready for harvest"
    },

    "harvesting": {
        "harvest_time": "When heads are firm and tight, usually 70–90 days",
        "method": "Use sharp knife to cut head, leave a few wrapper leaves for protection",
        "multiple harvests": "Harvest in batches to avoid over-mature heads",
        "expected_yield": "25–60 tons/ha depending on variety and care"
    },

    "post_harvest_handling": {
        "cleaning": "Remove damaged leaves, do not wash (encourages rot)",
        "grading": "Sort based on size and quality",
        "storage": "Cool, well-ventilated room; can store up to 3 weeks at 0°C–5°C",
        "transport": "Use crates to avoid bruising; avoid stacking"
    },

    "marketing_and_economics": {
        "value_addition": ["Pre-cut cabbage", "Coleslaw mixes", "Pickled cabbage (sauerkraut, kimchi)"],
        "best_markets": ["Urban markets", "Hotels", "Supermarkets", "Processing plants"],
        "pricing_tips": "Avoid gluts — stagger planting; contract farming can stabilize price",
        "cost_estimates": "Input cost can range $1,200–$1,800 per ha depending on fertilizer and pest control intensity"
    },

    "common_problems_and_solutions": {
        "splitting_heads": "Caused by excessive watering or over-maturity — harvest on time",
        "poor_head_formation": "Due to nitrogen deficiency or water stress",
        "pest_infestation": "Rotate crops and monitor weekly for early detection"
    },

    "smart_farming_tips": {
        "tools": [
            "Mobile pest ID apps (PlantVillage, FAO eLocust)",
            "Weather forecast alerts for spraying schedules",
            "Soil test kits for fertility planning"
        ],
        "record_keeping": [
            "Seed source and variety",
            "Fertilizer and spray dates",
            "Yield per batch",
            "Market price per kg"
        ]
    }
}
cassava_knowledge_base = {
    "crop_profile": {
        "botanical_name": "Manihot esculenta",
        "family": "Euphorbiaceae",
        "varieties": [
            "Sauti", "Mbundumali", "Kaleso", "TME 419", "Narocass 1", "Chila", "Mkumba", "Gauche"
        ],
        "maturity_days": "8 to 24 months depending on variety and purpose (sweet or bitter)",
        "uses": [
            "Human consumption (fresh, flour, gari)",
            "Animal feed",
            "Starch and ethanol production"
        ],
        "yield_potential": "15–35 tons/ha under good agronomic practices"
    },

    "climate_and_soil": {
        "temperature_range": "25°C to 30°C optimal",
        "rainfall_requirements": "1000–1500 mm annually; tolerates drought once established",
        "altitude_range": "0–1500 meters above sea level",
        "soil_type": "Well-drained sandy loam or loamy soils rich in organic matter",
        "soil_pH": "5.5 to 6.5",
        "tolerance": "Tolerates poor soils but not waterlogging",
        "land_preparation": {
            "clearing": "Remove bushes, tree stumps and perennial weeds",
            "ploughing_depth": "20–30 cm",
            "ridges_or_mounds": "Raised ridges or mounds spaced 1 m apart for better aeration and root development"
        }
    },

    "planting_material": {
        "type": "Stem cuttings (stakes) from mature plants (8–18 months old)",
        "length": "20–30 cm long, 5–8 nodes",
        "quality_check": "Free from disease, not woody or overly dry",
        "pre_planting_treatment": "Dip in fungicide or insecticide solution to prevent rot and pest attack"
    },

    "planting": {
        "best_time": "Start of rainy season or with irrigation",
        "spacing": "1 m x 1 m (10,000 plants/ha) or 0.9 m x 0.9 m for high-yielding systems",
        "planting_method": "Slanted or vertical planting with 2–3 nodes in the soil",
        "planting_depth": "5–10 cm"
    },

    "fertilizer_and_soil_health": {
        "organic_matter": "Apply compost or manure: 10–15 tons/ha",
        "inorganic": {
            "NPK": "Use NPK 15:15:15 at 200–300 kg/ha if soil is poor",
            "Top_dressing": "Apply Urea at 50–100 kg/ha at 8–10 weeks",
            "Potassium": "Apply MOP if soils are potassium-deficient (especially for root development)"
        },
        "liming": "Apply lime if soil pH is below 5.0"
    },

    "weed_and_soil_management": {
        "critical_weeding_period": "First 10–14 weeks",
        "manual_weeding": "2–3 timely weedings required",
        "intercropping": ["Maize", "Groundnut", "Beans"],
        "mulching": "Use organic mulch to retain moisture and suppress weeds"
    },

    "pest_and_disease_control": {
        "major_pests": {
            "cassava_mealybug": "Use resistant varieties, predators, and neem extract",
            "cassava_green_mite": "Plant early and use natural predators",
            "whiteflies": "Use yellow sticky traps or Imidacloprid",
            "termite_attack": "Use well-cured stakes and treat soil or cuttings with termiticides"
        },
        "major_diseases": {
            "cassava_mosaic_disease (CMD)": "Use resistant varieties and virus-free cuttings",
            "cassava_bacterial_blight": "Use clean planting material and rotate crops",
            "root_rot": "Ensure proper drainage and avoid planting in waterlogged areas",
            "brown_streak_disease": "Use tolerant varieties and control whiteflies"
        }
    },

    "growth_stages": {
        "1": "Establishment (0–2 months): root and shoot development",
        "2": "Vegetative growth (2–5 months): rapid shoot and leaf expansion",
        "3": "Tuber initiation (5–7 months): storage roots start to swell",
        "4": "Tuber bulking (7–12 months): roots mature and accumulate starch",
        "5": "Maturation (12–18 months): canopy begins to decline, ideal harvest window"
    },

    "harvesting": {
        "harvest_time": "Between 9–18 months depending on variety and market",
        "maturity_signs": "Yellowing and leaf fall, cracking soil, thick roots",
        "harvesting_method": "Uproot by hand or dig gently with hoe; cut stem first",
        "yield_expectation": "15–35 tons/ha under optimal conditions",
        "post_harvest_note": "Roots should be processed quickly (within 48 hrs) to avoid spoilage"
    },

    "post_harvest_handling": {
        "processing_methods": [
            "Chipping and drying",
            "Gari processing",
            "Fermentation (fufu/flour)",
            "Boiling and freezing"
        ],
        "storage": {
            "fresh_roots": "Store in pits lined with straw or cover in sand for up to 7 days",
            "dried_chips": "Store in moisture-proof bags in dry rooms"
        },
        "value_addition": [
            "Cassava flour",
            "Starch",
            "Bioethanol",
            "Animal feed",
            "Snacks (chips, biscuits)"
        ]
    },

    "marketing_and_economics": {
        "market_demand": ["Gari", "Cassava flour", "Fresh roots", "Starch"],
        "price_tips": "Process into value-added products for better profit",
        "transport": "Handle roots gently to prevent bruising and rot",
        "business_tip": "Form farmer groups for contract farming or cooperative marketing"
    },

    "common_problems_and_solutions": {
        "rotting_roots": "Avoid harvesting late; plant in well-drained soil",
        "poor_yield": "Check variety used, soil fertility, and weed control",
        "woody_roots": "Harvest on time (before 18 months), irrigate if drought stress occurs"
    },

    "smart_farming_tips": {
        "tools": [
            "GPS mapping for field layout",
            "Soil pH testing kits",
            "Mobile apps like PlantVillage or FAO's FAMEWS"
        ],
        "records_to_keep": [
            "Planting date",
            "Fertilizer applications",
            "Pest/disease outbreaks",
            "Harvest volume and quality"
        ]
    }
}
rice_knowledge_base = {
    "crop_profile": {
        "botanical_name": "Oryza sativa",
        "family": "Poaceae",
        "major_varieties": {
            "Irrigated": ["IR64", "Kilombero", "Supa", "TXD306"],
            "Rainfed lowland": ["NERICA", "Komboka"],
            "Upland": ["NERICA 4", "Kanyani"]
        },
        "maturity_days": "90–150 (variety-dependent)",
        "yield_potential": "3–10 tons/ha (with good management)"
    },
    "climate_and_soil": {
        "optimal_temperature_c": "25–35°C",
        "rainfall_mm": "1200–1500 (well distributed)",
        "soil_type": "Clay loam or loamy, well-drained for upland; heavy clay for irrigated",
        "soil_pH": "5.5–7.0",
        "land_preparation": {
            "upland": "Plough and harrow to fine tilth",
            "lowland": "Flood, puddle (wet tillage), level field"
        }
    },
    "seed_management": {
        "seed_rate_kg_per_ha": "40–60 (transplanting), 60–80 (direct sowing)",
        "treatment": "Soak seeds 24 hours, incubate 48 hours in warm cloth; fungicide (e.g., Thiram)",
        "germination_expectation": "≥90%",
        "nursery_preparation": {
            "area_needed": "500 m² nursery for 1 ha",
            "soil_mix": "Manure and topsoil",
            "watering": "Light irrigation daily"
        }
    },
    "planting": {
        "methods": {
            "transplanting": {
                "description": "Raise seedlings and transplant at 2–3 weeks",
                "spacing_cm": "20x20 or 25x25",
                "depth": "1–2 cm",
                "seedlings_per_hill": "2–3"
            },
            "direct_seeding": {
                "dry_seeding": "Mechanically or by hand; requires fine seedbed",
                "wet_seeding": "Broadcast presoaked seeds on puddled fields"
            }
        },
        "planting_time": {
            "rainfed": "Start of rains (Feb–Mar or Nov–Dec)",
            "irrigated": "Any time with water availability"
        }
    },
    "fertilizer_management": {
        "basal_application": {
            "NPK": "15:15:15 or 17:17:17 at 200–300 kg/ha before or at transplanting"
        },
        "top_dressing": [
            {"timing": "Tillering (2–3 weeks after planting)", "fertilizer": "Urea", "rate": "50 kg/ha"},
            {"timing": "Panicle initiation (6–7 weeks)", "fertilizer": "Urea", "rate": "50 kg/ha"}
        ],
        "organic_alternative": "Compost + biofertilizer inoculation"
    },
    "irrigation_and_water": {
        "requirement": "5000–8000 m³ per ha (irrigated)",
        "frequency": "Maintain 5 cm water depth until flowering",
        "drain_before_harvest": "2 weeks prior"
    },
    "weed_management": {
        "manual": "Hand weeding at 2 and 6 weeks",
        "chemical": {
            "pre_emergent": "Butachlor, Pendimethalin",
            "post_emergent": "2,4-D, Propanil"
        },
        "integrated_method": "Use of rice–fish farming or mulching in uplands"
    },
    "pest_and_disease": {
        "pests": {
            "rice_stem_borer": "Yellowing/dead hearts — use Carbofuran or biologicals",
            "rice_leaf_folder": "Folded leaves — spray Lambda-cyhalothrin",
            "rice_hispa": "Scratched leaves — remove infested leaves"
        },
        "diseases": {
            "blast": "Brown leaf spots — apply Mancozeb + good spacing",
            "bacterial_leaf_blight": "V-shaped yellowing — use resistant varieties",
            "sheath_rot": "Water-soaked lesions — improve aeration and drainage"
        }
    },
    "growth_stages": {
        "1": "Germination (0–10 days)",
        "2": "Seedling (10–25 days)",
        "3": "Tillering (25–45 days)",
        "4": "Panicle initiation (45–60 days)",
        "5": "Flowering (60–80 days)",
        "6": "Grain filling (80–100 days)",
        "7": "Maturity (100–150 days)"
    },
    "harvesting": {
        "maturity_signs": "90% of panicles turned golden yellow",
        "method": "Cut with sickle or combine harvester",
        "post_harvest": {
            "threshing": "Within 24 hours of harvest",
            "drying": "To 12–14% moisture content",
            "storage": "Use sealed bags, cool dry room"
        },
        "expected_yield": "4–6 t/ha (rainfed), up to 10 t/ha (irrigated)"
    },
    "marketing": {
        "grading": "Separate broken grains, foreign matter",
        "value_addition": "Parboiling, packaging, branding",
        "channels": ["farm gate", "rice millers", "cooperatives", "bulk buyers"]
    },
    "troubleshooting_faq": {
        "yellow_leaf_tips": "Possible nitrogen deficiency or salt stress",
        "patchy_germination": "Poor seed treatment or birds",
        "lodging": "Too much nitrogen or wind — use stronger varieties",
        "low_yield": "Check water stress, panicle emergence, pests"
    },
    "smart_tips": {
        "precision_farming": "Use drone or satellite tools for weed/pest maps",
        "mobile_tools": "PlantVillage Nuru app or RiceAdvice by AfricaRice",
        "record_keeping": "Track costs, dates, inputs and yield per plot"
    }
}
maize_knowledge_base = {
    "crop_profile": {
        "common_names": ["Maize", "Corn"],
        "botanical_name": "Zea mays",
        "growth_duration": "90–150 days (depends on variety and environment)",
        "yield_range": "2.5–10 tons/ha (up to 12 tons/ha with irrigation and high-input systems)",
        "economic_importance": [
            "Staple food in many countries",
            "Feed for livestock",
            "Raw material for industries (starch, ethanol, oil)"
        ]
    },

    "climate_and_soil_requirements": {
        "temperature": "Optimal: 18°C to 27°C; sensitive to frost",
        "rainfall": "500–800 mm well-distributed; needs moisture at flowering and grain filling",
        "soil_type": "Loamy soils with good structure and drainage",
        "soil_pH": "5.5–7.0",
        "altitude": "Sea level to 2,400 m (variety-dependent)"
    },

    "land_preparation": {
        "ploughing": "First deep plough (20–30 cm) to break compact layers",
        "harrowing": "Fine tilth required for good seed-soil contact",
        "ridges_or_beds": "Optional based on rainfall and drainage",
        "weed_control": "Pre-planting removal of invasive and perennial weeds",
        "soil_amendments": "Incorporate lime or organic matter based on soil test results"
    },

    "variety_selection": {
        "selection_criteria": [
            "Maturity period (early, medium, late)",
            "Tolerance to drought, low nitrogen, and diseases",
            "Yield potential",
            "Suitability to local climate"
        ],
        "recommended_varieties": {
            "early_maturing": ["MH26", "SC403"],
            "medium_maturing": ["SC627", "DK8053"],
            "late_maturing": ["SC719", "PAN 53"],
            "drought_tolerant": ["ZMS606", "ZM523"],
            "highland_varieties": ["MH31", "MH34"]
        }
    },

    "seed_and_planting": {
        "seed_rate": "20–25 kg/ha (depending on spacing and seed size)",
        "plant_spacing": {
            "row_spacing": "75 cm (rain-fed), 90 cm (irrigated)",
            "plant_spacing": "25–30 cm within the row"
        },
        "planting_depth": "5–7 cm (adjust based on soil moisture)",
        "planting_time": "At the onset of rains (ensure 3+ days of consistent moisture)",
        "seed_treatment": [
            "Fungicide (e.g., Thiram or Metalaxyl)",
            "Insecticide (e.g., Imidacloprid)",
            "Rhizobium inoculants not required for maize"
        ]
    },

    "fertilizer_management": {
        "organic_fertilizer": "5–10 tons/ha of well-rotted manure or compost",
        "chemical_fertilizer": {
            "basal": "200–300 kg/ha of NPK 23:21:0+4S",
            "top_dress_1": "Urea 150 kg/ha (applied 2–3 weeks after emergence)",
            "top_dress_2": "Urea 150 kg/ha (just before tasseling)"
        },
        "micronutrients": "Zinc and boron may be needed based on soil test",
        "split_application": "Improves nitrogen use efficiency and reduces leaching"
    },

    "weed_management": {
        "critical_period": "First 6 weeks after emergence",
        "manual_weeding": "At 2–3 weeks and again at 6–7 weeks",
        "herbicides": {
            "pre_emergence": "Atrazine + Metolachlor",
            "post_emergence": "Nicosulfuron or 2,4-D (careful with timing)"
        },
        "mulching": "Can be used to suppress weeds in conservation agriculture"
    },

    "irrigation_management": {
        "water_requirements": "450–600 mm (depends on climate)",
        "critical_stages": [
            "Germination",
            "Knee-high stage (vegetative growth)",
            "Tasseling and silking",
            "Grain filling"
        ],
        "methods": ["Furrow", "Drip", "Sprinkler"],
        "avoid_water_stress": "Especially during flowering and pollination"
    },

    "pest_and_disease_management": {
        "common_pests": {
            "fall_armyworm": "Control with Lambda-cyhalothrin, Emamectin benzoate, or biologicals like NPV",
            "stem_borers": "Apply systemic insecticides at whorl stage",
            "cutworms": "Soil treatment or baiting before planting",
            "aphids": "Control with insecticidal soap or Imidacloprid"
        },
        "common_diseases": {
            "maize_streak_virus": "Use resistant varieties; control leafhoppers",
            "northern_leaf_blight": "Fungicide application and resistant varieties",
            "gray_leaf_spot": "Rotate crops; avoid overhead irrigation",
            "downy_mildew": "Seed treatment and field sanitation"
        },
        "IPM_practices": [
            "Crop rotation",
            "Use pest-resistant varieties",
            "Timely scouting and threshold-based spraying",
            "Biological control using Trichogramma spp. or NPV"
        ]
    },

    "crop_management": {
        "thinning": "If more than one seed germinates per hole",
        "gapping": "Replant missing hills within 2 weeks",
        "earthing_up": "To support plants and reduce lodging",
        "topping": "Remove male flower (tassel) in some hybrids after pollination to reduce competition"
    },

    "harvesting": {
        "harvest_time": "When husks turn brown and cobs dry (~30% grain moisture)",
        "moisture_target": "13–14% for safe storage",
        "harvesting_methods": [
            "Manual: Dehusking and shelling",
            "Mechanical: Combine harvesters (in commercial farms)"
        ],
        "post_harvest": [
            "Drying: Sun-dry for 2–3 days after shelling",
            "Storage: Use airtight bags, silos, or PICS bags",
            "Protection: Treat with Actellic Super or use neem leaves to repel insects"
        ]
    },

    "post_harvest_utilization": {
        "uses": [
            "Food (flour, porridge, boiled corn)",
            "Animal feed (bran, silage)",
            "Industrial (ethanol, starch, sweeteners)"
        ],
        "value_addition": [
            "Maize meal, corn oil, snack production",
            "Packaging for retail markets",
            "Maize-based beverages or porridges"
        ],
        "marketing": [
            "Cooperatives or farmer associations",
            "Agro-dealers and processors",
            "Export if quality and moisture are well controlled"
        ]
    },

    "smart_farming_practices": {
        "soil_testing": "Before planting to inform fertilizer decisions",
        "GIS_mapping": "To optimize planting zones",
        "remote_sensing": "For detecting crop stress and disease",
        "mobile_advisory_tools": "For weather forecasts and spray alerts",
        "record_keeping": "Log inputs, rainfall, pest incidence, and yields"
    }
}

