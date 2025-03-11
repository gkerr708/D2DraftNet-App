from d2draftnet.embedding_model import DraftPredictionNN
from d2draftnet.config import TRAINED_MODEL_PATH, HERO_MAP, EMBEDDING_DIM, LAYERS, NUM_HEROS


if __name__ == "__main__":
    radiant_heroes = ["Lycan", "Enchantress", "Dragon Knight", "Lion", "Ember Spirit"]
    dire_heroes = ["Gyrocopter", "Terror Blade", "Bounty Hunter", "Earth Spirit", "Tinker"]

    model = DraftPredictionNN(num_heroes=NUM_HEROS, embedding_dim=EMBEDDING_DIM, dropout_prob=1e-3, layers=LAYERS)



