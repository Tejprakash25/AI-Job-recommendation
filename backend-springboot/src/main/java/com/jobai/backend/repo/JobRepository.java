package com.jobai.backend.repo;

import org.springframework.data.mongodb.repository.MongoRepository;
import com.jobai.backend.model.Job;

public interface JobRepository extends MongoRepository<Job, String> {
}
