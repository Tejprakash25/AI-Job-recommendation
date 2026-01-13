package com.jobai.backend.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AIService {

    public String getMatches() {
        RestTemplate rest = new RestTemplate();
        return rest.getForObject("https://ai-job-recommendation-jfcq.onrender.com/match", String.class);
    }
}
