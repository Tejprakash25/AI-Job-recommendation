package com.jobai.backend.model;

import org.springframework.data.annotation.Id;
import lombok.Data;

@Data
public class Job {
    @Id
    private String id;
    private String title;
    private String description;
}
