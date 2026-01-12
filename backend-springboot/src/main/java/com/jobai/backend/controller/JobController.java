package com.jobai.backend.controller;

import org.springframework.web.bind.annotation.*;
import com.jobai.backend.service.AIService;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api")
public class JobController {

    private final AIService ai;

    public JobController(AIService ai) {
        this.ai = ai;
    }

    @GetMapping("/recommendations")
    public String getRecommendations() {
        return ai.getMatches();
    }
}
