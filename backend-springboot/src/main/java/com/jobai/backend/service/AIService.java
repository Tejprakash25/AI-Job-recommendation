package com.jobai.backend.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AIService {

    public String getMatches() {
        RestTemplate rest = new RestTemplate();
        return rest.getForObject("http://127.0.0.1:8000/match", String.class);
    }
}
