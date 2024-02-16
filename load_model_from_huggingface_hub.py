import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, MT5EncoderModel
from transformers import PretrainedConfig, PreTrainedModel

class MTRankerConfig(PretrainedConfig):
    
	def __init__(self, backbone='google/mt5-base', **kwargs):
            self.backbone = backbone
            super().__init__(**kwargs)
            
	

class MTRanker(PreTrainedModel):
    config_class = MTRankerConfig

    def __init__(self, config):
        super().__init__(config)
        self.encoder = MT5EncoderModel.from_pretrained(config.backbone)
        self.num_classes = 2
        self.classifier = torch.nn.Linear(self.encoder.config.hidden_size, self.num_classes)
    
    def forward(self, input_ids, attention_mask):
        encoder_output = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        seq_lengths = torch.sum(attention_mask, keepdim=True, dim=1)
        pooled_hidden_state = torch.sum(encoder_output * attention_mask.unsqueeze(-1).expand(-1, -1, self.encoder.config.hidden_size), dim=1)
        pooled_hidden_state /= seq_lengths
        prediction_logit = self.classifier(pooled_hidden_state)
        return prediction_logit

tokenizer = AutoTokenizer.from_pretrained('ibraheemmoosa/mt-ranker-base')
model = MTRanker.from_pretrained('ibraheemmoosa/mt-ranker-base')
