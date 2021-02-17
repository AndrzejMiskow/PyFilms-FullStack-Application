package com.vaadin.tutorial.crm.backend.service;

import com.vaadin.tutorial.crm.backend.entity.Contact;
import com.vaadin.tutorial.crm.backend.repository.ContactRepository;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import java.util.List;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@Service 
public class ContactService {
	private static final Logger LOGGER = Logger.getLogger(ContactService.class.getName());
	private ContactRepository contactRepository;

	public ContactService(ContactRepository contactRepository) {
		this.contactRepository = contactRepository;
	}

	public List<Contact> findAll() {
		return contactRepository.findAll();
	}

	public long count() {
		return contactRepository.count();
	}

	public void delete(Contact contact) {
		contactRepository.delete(contact);
	}

	public void save(Contact contact) {
		if (contact == null) { 
			LOGGER.log(Level.SEVERE,
					"Contact is null. Are you sure you have connected your form to the application?");
			return;
		}
		contactRepository.save(contact);
	}


	//used for populating the tables with fake data
	@PostConstruct
	public void fillDb() {
		if (contactRepository.count() == 0) {
			Random r = new Random(0);
			contactRepository.saveAll(
					Stream.of("Lázaro Kovačević", "Acacius Senft", "Gismund Gorman",
							"Placidus Ottosson", "Robert Outrider")
							.map(name -> {
								String[] split = name.split(" ");
								Contact contact = new Contact();
								contact.setFirstName(split[0]);
								contact.setLastName(split[1]);
								return contact;
							}).collect(Collectors.toList()));
		}
	}
}